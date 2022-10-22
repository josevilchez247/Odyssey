FROM python:3.9-slim

LABEL maintainer="josevilchez247"

WORKDIR /app

COPY pyproject.toml* /app/

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

RUN adduser --disabled-password test

RUN chown -R test .

USER test

WORKDIR /app/test

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0

ENV PATH=$PATH:/home/test/.local/bin:/home/test/.poetry/bin
    
ENTRYPOINT ["poetry","run","test"]
