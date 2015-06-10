from locust import HttpLocust, TaskSet, task
from influxdb import InfluxDBClient

host = 'monitoring-influxdb'
port = 8086
user = 'root'
pw = 'root'

client = InfluxDBClient (host, port, user, pw, None)
databases = client.get_list_database()

if not any(val['name'] == 'results' for val in databases):
  client.create_database('results')
if not any(val['name'] == 'failures' for val in databases):
  client.create_database('failures')

def output_success_log (request_type, name, response_time, response_length, ** kw):
  client = InfluxDBClient (host, port, user, pw, 'results')
  json_body = [{
    "Points": [[request_type, name, response_time, response_length]],
    "Name": "loadtest_result",
    "Columns": ["request_type", "name", "response_time", "response_length"]
  }]
  client.write_points (json_body)

def output_failure_log (request_type, name, response_time, exception, ** kw):
  client = InfluxDBClient (host, port, user, pw, 'failures')
  json_body = [{
    "Points": [[request_type, name, response_time, exception]],
    "Name": "loadtest_result",
    "Columns": ["request_type", "name", "response_time", "exception"]
  }]
  client.write_points (json_body)

class JsonSerialization(TaskSet):
  @task(1)
  def json(self):
    self.client.get("/json")

class WebsiteUser(HttpLocust):
  task_set = JsonSerialization

events.request_success + = output_success_log 
events.request_failure + = output_failure_log 