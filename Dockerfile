FROM python:3-alpine

WORKDIR /src

ADD ./src /src

RUN apk --update add httpie && pip install -r requirements.txt

ENTRYPOINT ["python"]