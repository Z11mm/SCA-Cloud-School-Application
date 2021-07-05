# syntax=docker/dockerfile:1

# Choose base image
FROM python:3.9-slim-buster

# Choose working directory as default location for all commands
WORKDIR /app

# Copy file containing dependencies into image
COPY requirements.txt requirements.txt

# Install dependencies into image
RUN pip3 install -r requirements.txt

# Add source code files into image
COPY . .

# Run command to execute image within container
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]