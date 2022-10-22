FROM python:3.9-slim

LABEL maintainer="josevilchez247"

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

RUN adduser --disabled-password test

USER test

WORKDIR /app/test

ENV PATH=$PATH:/home/test/.local/bin

COPY pyproject.toml poetry.lock /app/

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0

RUN poetry config virtualenvs.create false; poetry install --only main
    
ENTRYPOINT ["poetry","run","test"]
