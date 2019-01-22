FROM python:3-alpine

ENV PYTHONPATH=.:$PYTHONPATH

WORKDIR /app

ADD . /app

RUN python setup.py develop

ENTRYPOINT ["bs"]