FROM python:2.7

RUN pip install locustio pyzmq
RUN ulimit -c -m -s -t unlimited
COPY scripts /scripts

ENTRYPOINT ["locust"]