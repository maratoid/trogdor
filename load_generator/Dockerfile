FROM debian:jessie
EXPOSE 8089

# Set the reset cache variable
ENV REFRESHED_AT 2015-06-8

ENV DEBIAN_FRONTEND noninteractive

# Update packages list
RUN apt-get update -y

# Install useful packages
RUN apt-get install -y build-essential libssl-dev

# Install required software
RUN apt-get install -y python python-dev python-distribute python-pip

# Install locust
RUN pip install pyzmq --install-option="--zmq=bundled"
RUN pip install locustio

# Cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Raise the limits to successfully run benchmarks
RUN ulimit -c -m -s -t unlimited

COPY scripts /scripts

ENV DEBIAN_FRONTEND=newt

ENTRYPOINT ["locust"]