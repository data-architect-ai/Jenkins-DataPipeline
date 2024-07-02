# Use the official Jenkins base image based on Debian
FROM jenkins/jenkins:latest

# Switch to root user to install packages
USER root

# Install Python and pip using apt-get (for Debian/Ubuntu)
RUN apt-get update \
    && apt-get install -y python3 python3-pip

# Switch back to Jenkins user
USER jenkins
