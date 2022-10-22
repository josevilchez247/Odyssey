FROM python:3.9-slim

LABEL maintainer="josevilchez247" version="1.0.0" 

RUN groupadd -g 1000 -r usertest && \
    useradd -u 1000 -m -r -g usertest usertest

USER usertest

WORKDIR /app/test/

ENV PATH=$PATH:/home/usertest/.local/bin

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
    pip install poethepoet && \
    poetry config virtualenvs.create false && \
    poetry install

ENTRYPOINT ["poe", "test"]
