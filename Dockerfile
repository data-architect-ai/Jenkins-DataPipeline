# Use the official Jenkins base image based on Debian
FROM jenkins/jenkins:latest

# Switch to root user to install packages
USER root

# Install Python 3 and pip using apt-get (for Debian/Ubuntu)
RUN apt-get update \
    && apt-get install -y python3 python3-pip

# Upgrade pip to the latest version (optional)
RUN pip3 install --upgrade pip

# Copy requirements.txt to the Docker image
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies from requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Switch back to Jenkins user
USER jenkins

# Optionally, you can continue configuring Jenkins or add additional steps here
