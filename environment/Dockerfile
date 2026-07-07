FROM python:3.13-slim-bookworm@sha256:129f9f5d5729767916d79f0021ba4fe56ff113332b08ef1213ecf529a9da7ebb

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
