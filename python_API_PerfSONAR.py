# https://www.dataquest.io/blog/python-api-tutorial/

import requests


response = requests.get("https://192.168.50.190/esmond/perfsonar/archive/")
print(response.status_code)

print(response.json())