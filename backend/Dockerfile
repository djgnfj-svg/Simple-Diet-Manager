FROM python:3.9.0

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y

ADD . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput


EXPOSE 8000