FROM python:3.8

LABEL agusrichard "agus.richard21@gmail.com"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www/auth-service

COPY ./auth-service /var/www/auth-service

RUN pip install -r /var/www/auth-service/requirements.txt