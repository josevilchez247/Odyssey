FROM python:3.9-slim

LABEL maintainer="josevilchez247"

RUN groupadd -g 1000 -r odyssey && \
    useradd -u 1000 -m -r -g odyssey odyssey

USER odyssey

ENV PATH=$PATH:/home/odyssey/.local/bin

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0

WORKDIR /app/test/

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

ENTRYPOINT ["poetry","run","test"]
