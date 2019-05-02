import requests


# click list
session = requests.Session()
session.auth = (u'adminuser', 'citusdata2019')
session.verify = False

clicks_request = session.get("http://127.0.0.1:8080/api/clicks/?limit=20&offset=0")
data = clicks_request.json()
print(data)


# click retrieve
session = requests.Session()
session.auth = (u'adminuser', 'citusdata2019')
session.verify = False

clicks_request = session.get("http://127.0.0.1:8080/api/clicks/00000b12-5340-4d81-9007-9e54516487d3/")
data = clicks_request.json()
print(data)
