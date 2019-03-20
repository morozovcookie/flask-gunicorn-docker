FROM python:3-alpine as base

FROM base as builder

RUN mkdir /install \
    && mkdir /static
COPY requirements.txt /requirements.txt
COPY flask_gunicorn_docker/static /static
WORKDIR /static
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
        postgresql-dev \
        libffi-dev \
        gcc \
        python3-dev \
        musl-dev \
        nodejs \
        nodejs-npm \
    && pip install --no-cache-dir --install-option="--prefix=/install" -r /requirements.txt \
    && npm install -g yarn \
    && yarn install \
    && yarn build

FROM base

COPY --from=builder /install /usr/local
RUN apk --no-cache add libpq

COPY flask_gunicorn_docker /flask-gunicorn-docker/flask_gunicorn_docker
COPY --from=builder /static/build /flask-gunicorn-docker/flask_gunicorn_docker/static/build

WORKDIR /flask-gunicorn-docker/flask_gunicorn_docker

ENV PYTHONPATH /flask-gunicorn-docker

EXPOSE 80
