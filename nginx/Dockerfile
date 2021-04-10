# Nginx Dockerfile

# Base
FROM nginx:latest

# Commands
RUN mkdir -p /opt/web/
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d