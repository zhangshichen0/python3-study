# 对urllib3进行使用

import urllib3
import requests


requests.packages.urllib3.disable_warnings()
http = urllib3.PoolManager()

res = http.request('GET', "www.baidu.com")
print(res.status)
print(res.data.decode())
