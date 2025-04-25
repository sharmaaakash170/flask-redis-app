# ─── Stage 1: Build ────────────────────────────────────────────────────────────
FROM python:3.13-slim AS builder

WORKDIR /app

# Copy and install only Python dependencies first to leverage cache
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# ─── Stage 2: Runtime ──────────────────────────────────────────────────────────
FROM python:3.13-slim

WORKDIR /app

# Copy installed packages from the builder image
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your application code
COPY --from=builder /app /app

# Create a non-root user and take ownership of /app
RUN addgroup --system app \
 && adduser --system --ingroup app app \
 && chown -R app:app /app

USER app

# Ensure any pip-installed binaries are on PATH
ENV PATH=/usr/local/bin:$PATH

# Default command
CMD ["python", "app.py"]
