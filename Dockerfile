# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the server script into the container
COPY auth_server.py .

# Install the required dependencies
RUN pip install flask

# Expose the port the server will be listening on
EXPOSE 5000

# Set the command to run the server
CMD ["python", "auth_server.py"]