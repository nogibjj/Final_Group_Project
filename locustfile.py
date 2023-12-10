from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)  # This task will be executed 3 times more than the above task
    def load_dashboard(self):
        self.client.get("/dashboard")

    @task
    def post_something(self):
        self.client.post("/submit", {"key": "value"})
