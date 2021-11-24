from locust import HttpUser, TaskSet, task
import os

class WebsiteTasks(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")

class WebsiteUser(HttpUser):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000


if __name__ == "__main__":
    os.system('locust -f locustfile.py')
