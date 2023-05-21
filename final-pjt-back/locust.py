from locust import HttpUser, task, between
import random

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")