# https://www.dataquest.io/blog/python-api-tutorial/
# https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script


import requests


# response = requests.get("https://192.168.50.190/esmond/perfsonar/archive/")
# print(response.status_code)

# print(response.json())

url     = 'https://192.168.50.190/esmond/perfsonar/archive/'
payload = { 'key' : 'val' }
headers = {}
res = requests.post(url, data=payload, headers=headers)

print(res)