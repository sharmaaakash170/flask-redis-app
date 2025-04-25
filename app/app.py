from flask import Flask, jsonify
import requests
import redis
import json
import psycopg2
import os

app = Flask(__name__)
# Redis client
cache = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT"))
)

# Postgres connection
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
cur = conn.cursor()
# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        key TEXT UNIQUE,
        value TEXT
    )
""")
conn.commit()

@app.route('/add/<key>/<value>')
def add_message(key, value):
    cur.execute("INSERT INTO messages (key, value) VALUES (%s, %s) ON CONFLICT (key) DO NOTHING", (key, value))
    conn.commit()
    return f"Added ({key}, {value}) to database!"

@app.route('/get/<key>')
def get_message(key):
    cached_value = cache.get(key)
    if cached_value:
        return f"From cache: {cached_value.decode('utf-8')}"

    cur.execute("SELECT value FROM messages WHERE key = %s", (key,))
    row = cur.fetchone()
    if row:
        value = row[0]
        cache.set(key, value)
        return f"From DB (now cached): {value}"
    else:
        return "Key not found"

@app.route('/posts/<int:post_id>')
def get_post(post_id):
    cached_data = cache.get(f'post:{post_id}')
    if cached_data:
        return jsonify({'source': 'cache', 'data': json.loads(cached_data)})

    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    if response.status_code == 200:
        cache.setex(f'post:{post_id}', 60, json.dumps(response.json()))
        return jsonify({'source': 'api', 'data': response.json()})
    else:
        return jsonify({'error': 'Post not found'}), 404

@app.route('/invalidate/<int:post_id>', methods=['POST'])
def invalidate(post_id):
    key = f'post:{post_id}'
    if cache.delete(key):
        return jsonify({'status': 'invalidated', 'post_id': post_id}), 200
    return jsonify({'status': 'not found', 'post_id': post_id}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
