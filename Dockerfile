# Use an official Python runtime as a parent image
FROM python:3.12.2-slim

# Set the working directory to /app
WORKDIR /python-docker

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN apt-get -y install libsndfile1
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
