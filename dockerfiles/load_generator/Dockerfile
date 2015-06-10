FROM python:2.7

RUN pip install locustio pyzmq
COPY scripts /scripts

ENTRYPOINT ["locust"]