import datetime

import requests


# click retrieve
session = requests.Session()
session.auth = (u'adminuser', 'citusdata2019')
session.verify = False

data = {'ads': 1,
        'site_url': 'ha_test',
        'cost_per_click_usd': 1,
        'user_ip': '127.0.0,1',
        'clicked_at': datetime.datetime.now()
}
clicks_request = session.post("http://127.0.0.1:8080/api/clicks/", data=data)
