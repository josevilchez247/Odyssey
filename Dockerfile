FROM python:3.9-slim

LABEL maintainer="josevilchez247"

ENV POETRY_HOME="/opt/poetry"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0

WORKDIR /app/test/

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

ENTRYPOINT ["poetry","run","test"]
