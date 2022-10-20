FROM python:3.9-slim

LABEL maintainer="josevilchez247"

ENV POETRY_VERSION=1.2.0  \
    POETRY_HOME="/opt/poetry" \
    VENV_PATH="/opt/pysetup/.venv" 

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app/test/

COPY pyproject.toml /app/

RUN poetry install --no-dev

ENTRYPOINT ["poetry","run","test"]
