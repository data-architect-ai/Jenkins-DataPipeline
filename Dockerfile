# Use the official Jenkins base image based on Debian
FROM jenkins/jenkins:latest

# Switch to root user to install packages
USER root

# Install Python 3 and pip using apt-get (for Debian/Ubuntu)
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-venv

# Copy requirements.txt to the Docker image
COPY requirements.txt /tmp/requirements.txt

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies from requirements.txt
RUN pip install -r /tmp/requirements.txt

# Switch back to Jenkins user
USER jenkins

