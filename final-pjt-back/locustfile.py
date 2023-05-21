from locust import HttpUser, task, between, LoadTestShape
import random

class LocustUser(HttpUser):
    wait_time = between(3,4)
    # searchq = ['Locust부하테스트','SSAFY인적성','삼성전자입사']

    @task(1)
    def index(self):
        # self.client.get('https://www.google.com/search?q=%s%27%(random.choice(self.searchq)))
        self.client.get('http://localhost:8080/%27')