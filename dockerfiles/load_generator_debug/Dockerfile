FROM python:2.7

RUN pip install locustio pyzmq influxdb
RUN pip install --upgrade influxdb
RUN ulimit -c -m -s -t unlimited
COPY scripts /scripts

ENTRYPOINT ["locust"]