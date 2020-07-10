FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /airport_server

WORKDIR /airport_server

COPY . /airport_server

RUN pip install -r requirements.txt