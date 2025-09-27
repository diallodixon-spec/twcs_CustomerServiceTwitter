# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first (better build caching)
COPY requirements.txt .

# Install dependencies without cache to keep image small
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the ingestion script into the container
COPY ingestion.py .

# Default command: run ingestion script
CMD ["python3.11", "ingestion.py"]

