FROM python:3.9-slim

LABEL maintainer="josevilchez247"

RUN groupadd -r testuser && useradd -m -r -g testuser testuser

USER testuser

WORKDIR /home/testuser

COPY pyproject.toml ./

ENV PATH=$PATH:/home/testuser/.local/bin

RUN pip3 install poetry; poetry config virtualenvs.create false; poetry install

ENTRYPOINT ["poetry","run","test"]
