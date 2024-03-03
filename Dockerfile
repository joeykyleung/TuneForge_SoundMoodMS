# Use an official Python runtime as a parent image
FROM python:3.12.2-slim

# Set the working directory to /app
WORKDIR /project

# Copy the current directory contents into the container at /app
COPY . /project

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
