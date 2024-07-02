FROM jenkins/jenkins:latest

USER root

RUN apt-get update \
    && apt-get install -y python3 python3-pip

RUN apk update \
    && apk add --no-cache python3

USER jenkins
