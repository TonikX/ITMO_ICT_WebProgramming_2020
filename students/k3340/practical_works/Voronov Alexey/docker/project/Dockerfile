FROM python:3.6.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /project

WORKDIR /project

COPY . /project

RUN pip3 install -r requirements.txt
