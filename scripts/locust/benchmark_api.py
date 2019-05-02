import datetime
from locust import HttpLocust, TaskSet, task


def login(l):
    l.client.post("/login", {"username":"adminuser", "password":"citusdata2019"})

def logout(l):
    l.client.get("/logout")


class ApiBehavior(TaskSet):
    @task(1)
    def clicks(self):
        self.client.get("/api/clicks/?limit=20&offset=0", auth=('adminuser', 'citusdata2019'))

    @task(2)
    def click_detail(self):
        self.client.get("/api/clicks/00000b12-5340-4d81-9007-9e54516487d3/", auth=('adminuser', 'citusdata2019'))

    @task(3)
    def create_click(self):
        data = {'ads': 1,
                'site_url': 'ha_test',
                'cost_per_click_usd': 1,
                'user_ip': '127.0.0,1',
                'clicked_at': datetime.datetime.now()
        }
        self.client.post("/api/clicks/", data, auth=('adminuser', 'citusdata2019'))



class ApiUser(HttpLocust):
    task_set = ApiBehavior
    min_wait = 5000
    max_wait = 9000
