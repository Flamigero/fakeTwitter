FROM python:3.8-alpine

ENV PYTHONBUFFERED=1

# Install dependecies
RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client

WORKDIR /app

# Requirements
COPY requeriments.txt /app/
RUN pip install -r requeriments.txt

# Entrypoint
COPY init.sh /app/
RUN chmod +x init.sh

COPY . /app/