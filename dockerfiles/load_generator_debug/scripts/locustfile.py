import logging
import pprint
from locust import HttpLocust, TaskSet, task

# Uncomment to enable pushing results and failures into k8s influx database
"""from locust import events
from influxdb.influxdb08 import InfluxDBClient

host = 'monitoring-influxdb'
port = 8086
user = 'root'
pw = 'root'

client = InfluxDBClient (host, port, user, pw, 'k8s')

def output_success_log (request_type, name, response_time, response_length, ** kw):
  json_body = [{
    "Points": [[request_type, name, response_time, response_length]],
    "Name": "loadtest_results",
    "Columns": ["request_type", "name", "response_time", "response_length"]
  }]
  client.write_points (json_body)

def output_failure_log (request_type, name, response_time, exception, ** kw):
  json_body = [{
    "Points": [[request_type, name, response_time, exception]],
    "Name": "loadtest_failures",
    "Columns": ["request_type", "name", "response_time", "exception"]
  }]
  client.write_points (json_body)"""

class JsonSerialization(TaskSet):
  @task(1)
  def json(self):
    with self.client.get("/json", catch_response=True) as response:
      logging.info('Response headers:')
      logging.info(pprint.pformat(response.headers, 2))
      logging.info('Response content:')
      logging.info(response.content)

class WebsiteUser(HttpLocust):
  task_set = JsonSerialization

# Uncomment to enable pushing results and failures into k8s influx database
"""events.request_success += output_success_log 
events.request_failure += output_failure_log"""