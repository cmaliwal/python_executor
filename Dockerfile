# Use an official Python image as a base
FROM python:3.10-slim


# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    protobuf-compiler \
    libprotobuf-dev \
    libnl-route-3-dev \
    libseccomp-dev \
    libcap-dev \
    libz-dev \
    libssl-dev \
    pkg-config \
    iproute2 \
    iputils-ping \
    flex \
    bison

RUN rm -rf /var/lib/apt/lists/*

# Clone and build nsjail
RUN git clone https://github.com/google/nsjail /nsjail && cd /nsjail && make -j$(nproc)

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Print the contents of requirements.txt for debugging
RUN cat /app/requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the nsjail configuration file
COPY nsjail.cfg /etc/nsjail/nsjail.cfg

# Expose the port the app runs on
EXPOSE 8080

# Command to run the Flask app
CMD ["python", "main.py"]
