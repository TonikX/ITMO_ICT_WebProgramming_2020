FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /library-server

WORKDIR /library-server

COPY . /library-server

RUN pip install -r requirements.txt