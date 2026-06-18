from locust import HttpUser, task


class RetailPulseUser(HttpUser):

    host = "http://localhost:8501"

    @task
    def home(self):
        self.client.get("/")