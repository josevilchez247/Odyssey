FROM python:3.8-slim

LABEL maintainer="josevilchez247" version="1.2.0" 

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

# Crear usuario que ejecutará el contenedor y el grupo al que pertenece
RUN groupadd -r usertest && useradd -m --no-log-init -r -g usertest usertest

# Usuario que ejecuta el contenedor
USER usertest

# Copiar pyproject.toml y poetry.lock para poder instalar dependencias más tarde
COPY pyproject.toml poetry.lock /app/

# Añadir .local/bin al PATH para incluir instalación de scripts
# como poe por ejemplo
ENV PATH="$PATH:/home/usertest/.local/bin:${PATH}"

# Cambiar a directorio de trabajo para la instalación
WORKDIR /app/test

# Instalar herramientas necesarias para el proyecto (poetry y poethepoet)
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.1.15 && \
    poetry config virtualenvs.create false && \
    poetry install

# Pasar los tests
ENTRYPOINT ["poe", "test"]
