FROM python:3.9-slim

LABEL maintainer="josevilchez247"

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.2.2
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0

COPY pyproject.toml /app/

WORKDIR /app/test/

RUN poetry install --no-dev

ENTRYPOINT ["poetry","test"]
