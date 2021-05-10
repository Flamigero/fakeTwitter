FROM python:3.8-alpine

ADD ./tests/ /tests
WORKDIR /tests

# Requeriments
COPY /tests/requirements.txt /tests/
RUN pip install -r requirements.txt