FROM mcr.microsoft.com/playwright/python:v1.53.0-noble

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1

COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --locked --no-dev

COPY . .

