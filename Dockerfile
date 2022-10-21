FROM python:3.8-slim

LABEL maintainer="josevilchez247"

WORKDIR /app

COPY pyproject.toml /app/

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

RUN adduser --disabled-password test

RUN ln -s /usr/bin/python /usr/bin/python3.8; addgroup -S testgroup && adduser -S test -G testgroup

USER test

WORKDIR /app/test

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0

ENV PATH=$PATH:/home/test/.local/bin:/home/test/.poetry/bin

RUN  poetry config virtualenvs.create false; poetry installdeps --dev
    
ENTRYPOINT ["poetry","run","test"]
