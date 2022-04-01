FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /Intership_project

COPY . /Intership_project
RUN apt-get update && apt-get install -y netcat
RUN pip install pipenv && pipenv install --ignore-pipfile --system
