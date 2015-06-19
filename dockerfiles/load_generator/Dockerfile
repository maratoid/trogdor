FROM python:2.7

ENV INFLUXDB_HOST influxdb
ENV INFLUXDB_PORT 8086
ENV INFLUXDB_USER root
ENV INFLUXDB_PASSWORD root
ENV INFLUXDB_NAME k8s

RUN pip install locustio pyzmq influxdb
RUN pip install --upgrade influxdb
RUN ulimit -c -m -s -t unlimited
COPY scripts /scripts

ENTRYPOINT ["locust"]
