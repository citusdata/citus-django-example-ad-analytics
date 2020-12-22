import datetime
from locust import HttpUser, TaskSet, task


def login(l):
    l.client.post("/login/", {"username":"adminuser", "password":"citusdata2019"})

def logout(l):
    l.client.get("/logout/")

class UserBehavior(TaskSet):
    def login(self):
        # login to the application
        response = self.client.get('/login/')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/login/',
                         {'username': 'adminuser', 'password': 'citusdata2019'},
                         headers={'X-CSRFToken': csrftoken})

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def campaigns(self):
        self.client.get("/campaigns/")

    @task(3)
    def campaign_detail(self):
        self.client.get("/campaigns/1/")



class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
