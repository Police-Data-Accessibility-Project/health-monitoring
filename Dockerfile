FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1

COPY pyproject.toml uv.lock ./

# Install dependencies
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN uv sync --locked --no-dev

COPY . .
