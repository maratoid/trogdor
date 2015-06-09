from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def json(self):
        self.client.get("/json")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior