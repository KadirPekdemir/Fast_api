# Use the official Python image as the base image
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . /app/

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
