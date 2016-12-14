FROM ubuntu:14.04

MAINTAINER Xoriant <admin@xoriant.com>

RUN apt-get update

RUN apt-get install -y --force-yes -q nginx

COPY index.html /usr/share/nginx/html/

ENTRYPOINT ["/usr/sbin/nginx","-g","daemon off;"]

EXPOSE 80