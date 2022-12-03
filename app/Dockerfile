FROM python:3.9-slim

# set working directory inside a container
WORKDIR /usr/src/app

# install less text viewer to view the help
RUN apt-get update && apt-get install less -y

# copy requirements.txt to the working directory
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy everything to the working directory
COPY . .

# The command is executed when the container starts
ENTRYPOINT ["/bin/sh","-c","sleep 3600"]
