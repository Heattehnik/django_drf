FROM python:3

LABEL authors="roman"

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .