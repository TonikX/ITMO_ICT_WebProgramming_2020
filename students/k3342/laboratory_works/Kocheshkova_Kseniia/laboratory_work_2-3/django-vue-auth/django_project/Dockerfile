FROM python:3.8.1

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_project

WORKDIR /django_project

COPY . /django_project

RUN pip3 install -r requirements.txt