FROM python:3-slim
RUN adduser --disabled-password odyssey
WORKDIR /app
RUN chown -R odyssey .
USER odyssey
COPY --chown=odyssey pyproject.toml ./
WORKDIR /app/test
ENTRYPOINT ["poe","run","test"]
