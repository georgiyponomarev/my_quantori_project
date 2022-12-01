FROM python:3.9-slim

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN chmod a+x run.sh

# The command is executed when the container starts
ENTRYPOINT ["/bin/sh","-c","sleep 3600"]
