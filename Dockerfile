FROM python:3.9-slim

LABEL maintainer="josevilchez247"

WORKDIR /app
COPY ./pyproject.toml /app/

RUN groupadd -r testuser && useradd -m -r -g testuser testuser
USER testuser
WORKDIR /app/test

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --version 1.2.0

ENV PATH=$PATH:/home/test/.local/bin:/home/test/.poetry/bin

RUN  poetry config virtualenvs.create false; poetry installdeps --dev

ENTRYPOINT ["poetry","run","test"]
