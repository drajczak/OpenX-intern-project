from locust import HttpUser, task, between

class QuickStartUser(HttpUser):
    host = "dr-temperature-app"  # Kubernetes host name
    wait_time = between(1, 2.5)

    @task
    def my_task(self):
        self.client.get("/my-endpoint")
