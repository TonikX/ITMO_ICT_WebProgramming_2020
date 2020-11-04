FROM python:3.8.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project_library

RUN pip install --upgrade pip

COPY ./requirements.txt /project_library/requirements.txt
RUN pip install -r /project_library/requirements.txt

COPY . /project_library

EXPOSE 8000