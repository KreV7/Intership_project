FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /Intership_project

COPY . /Intership_project

RUN pip install pipenv && pipenv install --ignore-pipfile --system

CMD ./entrypoint.sh