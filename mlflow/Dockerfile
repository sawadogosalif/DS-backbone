# Use the official Python image as the base image
FROM python:3.10.14-slim

# Copy the requirements.txt file into the container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
