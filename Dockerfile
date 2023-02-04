# Use python base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . .

# Install the PyZMQ library
RUN pip install --no-cache-dir pyzmq

# Run the server application
CMD ["python", "server_prices.py"]