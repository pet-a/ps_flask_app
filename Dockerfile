FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get -y install git

FROM python:3.8

WORKDIR /ps_flask_app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .app/ .app/



CMD [ "python", "./app/flask_app.py" ]