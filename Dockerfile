FROM python:3-alpine

RUN mkdir -p /flask-gunicorn-docker
WORKDIR /flask-gunicorn-docker

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD ./flask-gunicorn-docker .

EXPOSE 80
