# Use the official Python image as the base
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Specify the command to run when the container starts
CMD ["python", "app.py"]

