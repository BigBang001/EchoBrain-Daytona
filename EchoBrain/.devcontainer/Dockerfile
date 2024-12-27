# Use a Python base image (compatible with TensorFlow)
FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

# Install necessary system dependencies for OpenCV, audio, etc.
RUN apt-get update && apt-get install -y \
    libgtk2.0-0 \
    libopencv-dev \
    python3-opencv \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /workspace

# Copy the requirements file into the container
COPY requirements.txt /workspace/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables if needed (optional)
ENV PYTHONUNBUFFERED=1

# Expose necessary ports (if you want to expose ports for the app)
EXPOSE 5000

# Set the default command to start the app
CMD ["python", "main.py"]