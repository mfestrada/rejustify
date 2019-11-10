FROM python:3.8.0-alpine3.10

COPY . /workdir
WORKDIR /workdir

RUN python setup.py install
