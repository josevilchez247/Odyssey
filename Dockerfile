FROM python:3.9-slim

LABEL maintainer="josevilchez247"

WORKDIR /app
COPY ./pyproject.toml /app/

RUN useradd -m -r -g testuser testuser
USER testuser
WORKDIR /app/test

RUN wget -q -O - "$@" https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH=$PATH:/home/test/.local/bin:/home/test/.poetry/bin

RUN  poetry config virtualenvs.create false; poetry installdeps --dev

ENTRYPOINT ["poetry","run","test"]
