FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /config

COPY requirements /config/requirements

RUN pip install -r /config/requirements/base.txt
RUN mkdir /src

COPY . /src

WORKDIR /src
