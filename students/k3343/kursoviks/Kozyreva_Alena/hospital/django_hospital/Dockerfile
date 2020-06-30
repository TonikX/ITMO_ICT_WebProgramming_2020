FROM python:3.6.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_hospital

WORKDIR /django_hospital

COPY . /django_hospital

RUN pip3 install -r requirements.txt
