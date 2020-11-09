FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY req.txt /backend/
RUN python3 -m pip install --pre --upgrade -r req.txt
COPY . /backend/

