FROM python:3.9.1

# Updates
RUN apt update
RUN apt-get -y install tesseract-ocr
RUN apt-get install tesseract-ocr-ben

ADD tests /tests
WORKDIR /tests

# Requirements
RUN pip install -r requirements.txt