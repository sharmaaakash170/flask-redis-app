
# Flask + Redis + PostgreSQL Dockerized Application

This project demonstrates how to build a simple web application using **Flask**, **Redis**, and **PostgreSQL** and containerize it using **Docker Compose**. The goal is to create a full-stack solution with a message caching system and persistent data storage, suitable for both development and production environments.

## Features

- **Flask** for building the web application.
- **Redis** for caching messages for faster responses.
- **PostgreSQL** for persistent storage of data.
- **Docker Compose** for managing multi-container Docker applications.
- Optimized **multi-stage Dockerfiles** to reduce image size.
- **CI/CD Integration** with automated build and deployment (Optional for future steps).
- **Development environment** with easy setup using `.env` configuration files.

## Technologies Used

- **Flask**: Lightweight Python web framework.
- **Redis**: In-memory data structure store used for caching.
- **PostgreSQL**: Relational database used for data persistence.
- **Docker**: Platform to create, deploy, and run containers.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.
- **Python**: Programming language used for building the application.

## Project Structure

```
flask-redis-app/
├── app.py                  # Flask app logic
├── Dockerfile              # Dockerfile for Flask app
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (for local dev)
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites

Make sure you have the following tools installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (with Docker Compose)
- [Python](https://www.python.org/) (for testing locally)

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sharmaaakash170/flask-redis-app.git
   cd flask-redis-app
   ```

2. **Build and run the containers**:
   Use Docker Compose to build and start the services (Flask, Redis, and PostgreSQL):
   ```bash
   docker-compose up --build
   ```

3. **Access the app**:
   Once the containers are up and running, you can access the app at `http://localhost:5000`.

4. **Stop the containers**:
   When you're done, you can stop the containers by running:
   ```bash
   docker-compose down
   ```

### Environment Variables

For local development, you can modify the `.env` file to set the PostgreSQL and Redis connection settings.

Example `.env` file:

```
DB_HOST=db
DB_PORT=5432
DB_NAME=flask_db
DB_USER=postgres
DB_PASSWORD=mysecretpassword
REDIS_HOST=redis
REDIS_PORT=6379
```

### Docker Compose Services

This project uses the following services in Docker Compose:

- **web**: The Flask app, which connects to Redis and PostgreSQL.
- **db**: PostgreSQL container for persistent storage.
- **redis**: Redis container for caching.

## Optimizations

### Multi-Stage Dockerfile

The Dockerfile uses a multi-stage build process:

1. **Builder stage**: Installs dependencies and packages.
2. **Runtime stage**: Creates a minimal image with the necessary runtime environment.

This reduces the size of the final image, which is ideal for both local and production environments.

## Next Steps

- **CI/CD Integration**: Integrate with Jenkins, GitHub Actions, or GitLab CI for automated builds and tests.
- **Private Docker Registry**: Set up a private Docker registry (e.g., Harbor or Docker Hub) for storing images.
- **Scaling**: Learn about Docker Swarm or Kubernetes to scale the application.

## Contributing

Feel free to fork the repository, submit issues, or open pull requests to improve the project.

## License

This project is open source and available under the MIT License.

---

Happy coding! 🚀
