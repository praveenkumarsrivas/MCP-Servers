# Use the official Python slim image as a base
FROM python:3.12-slim-bookworm

# Install curl (required for your tool) and ca-certificates (for HTTPS)
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Install uv (the Python package manager)
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Make sure uv is in the PATH
ENV PATH="/root/.local/bin:${PATH}"

# Set the working directory
WORKDIR /app

# Copy only dependency files first for better caching
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies in a virtual environment using uv
RUN uv venv .venv && uv pip install -r pyproject.toml

# Copy the rest of your application code
COPY . .

# Ensure the venv is used by default
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port if your server listens on one (optional, e.g., 8000)
# EXPOSE 8000

# Run the server using uv in the virtual environment
CMD ["uv", "run", "server.py"]