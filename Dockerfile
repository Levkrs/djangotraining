# Geek staff Dockerfile

# Base
FROM python:3.8-slim

# Commands
RUN mkdir -p /opt/app/
WORKDIR /opt/app/
COPY . /opt/app/
RUN pip3 install pip --upgrade && pip install --no-cache-dir -r reqs.txt
RUN chmod a+x ./run.sh

# Ports
EXPOSE 8001