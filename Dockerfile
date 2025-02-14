FROM python:3.12-bookworm

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
COPY . .
