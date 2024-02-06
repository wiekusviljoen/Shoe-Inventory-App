FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY inventory.py .
COPY inventory.txt .


# Install required modules
RUN pip install tabulate



# Run inventory.py when the container launches
CMD ["python", "-i", "inventory.py"]
