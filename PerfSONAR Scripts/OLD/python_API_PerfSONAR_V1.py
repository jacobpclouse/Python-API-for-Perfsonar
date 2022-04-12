# https://www.dataquest.io/blog/python-api-tutorial/
# https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
# https://docs.perfsonar.net/esmond_api_python.html


""" PERFSONAR CODE
from esmond.api.client.perfsonar.query import ApiConnect, ApiFilters

filters = ApiFilters()

filters.verbose = True
filters.time_start = time.time() - 3600
filters.time_end = time.time()
filters.source = '192.168.50.190'
filters.tool_name = 'pscheduler/iperf3'
filters.timeout = 5
filters.ssl_verify = False #allows self-signed https certificate

conn = ApiConnect('https://localhost/', filters)
"""

import requests
import datetime
# Use os.path to write output to different directory
import os.path


output_path = './Output/'
name_of_output_file=f'Output-.json'
#name_of_output_file=f'Output-{datetime.datetime.now()}.json'
full_path_and_filename = os.path.join(output_path, name_of_output_file)

url     = 'https://192.168.50.190/esmond/perfsonar/archive/'
payload = { 'key' : 'val' }
headers = {}
# SSL allow unsigned cert: -- DON'T DO THIS IF YOU DON'T FULLY TRUST THE SERVER
# https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
res = requests.get(url, data=payload, headers=headers, verify=False)


# print(response.status_code)
# print(response.json())

print(res)
print(datetime.datetime.now())
#Writing to file
# https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
##with open(full_path_and_filename, 'a') as f:
with open(full_path_and_filename, 'w') as f:
    print(res.json(), end = '', file=f)

