FROM python:3.9-slim

LABEL maintainer="josevilchez247"

RUN groupadd -g 1000 -r odyssey && \
    useradd -u 1000 -m -r -g odyssey odysey

USER odyssey

WORKDIR /app/test/

ENV PATH=$PATH:/home/odyssey/.local/bin

COPY pyproject.toml /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

ENTRYPOINT ["poe","test"]
