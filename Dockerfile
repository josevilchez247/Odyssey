FROM python:3.9-slim

LABEL maintainer="josevilchez247" version="1.2.0" 

# Crear usuario que ejecutará el contenedor y el grupo al que pertenece
RUN groupadd -r usertest && useradd -m --no-log-init -r -g usertest usertest

# Usuario que ejecuta el contenedor
USER usertest

# Copiar pyproject.toml y poetry.lock para poder instalar dependencias más tarde
COPY pyproject.toml poetry.lock ./

# Cambiar a directorio de trabajo para la instalación
WORKDIR /app/test

# Añadir .local/bin al PATH para incluir instalación de scripts
# como poe por ejemplo
ENV PATH="$PATH:/home/usertest/.local/bin:${PATH}"

# Mejorar la versión de pip: eliminar warnings
RUN python -m pip install --upgrade pip

# Instalar herramientas necesarias para el proyecto (poetry y poethepoet)
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

# Pasar los tests
ENTRYPOINT ["poe", "test"]
