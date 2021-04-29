FROM python:3.8

LABEL agusrichard "agus.richard21@gmail.com"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www/new-service

COPY ./new-service /var/www/new-service

RUN pip install -r /var/www/new-service/requirements.txt