FROM python:3.8

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY .env .
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000