# *** MAIN PERFSONAR REST API DOCUMENTATION: https://docs.perfsonar.net/esmond_api_rest.html ***

# https://www.dataquest.io/blog/python-api-tutorial/
# https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
# https://docs.perfsonar.net/esmond_api_python.html
# Python Filters: https://www.programiz.com/python-programming/methods/built-in/filter

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

# Imports
import json
from urllib.request import urlopen
import datetime

from esmond_client.perfsonar.query import ApiConnect, ApiFilters

filters = ApiFilters()

filters.verbose = True
filters.time_start = time.time() - 3600
filters.time_end = time.time()
filters.source = '192.168.50.190'
filters.tool_name = 'pscheduler/iperf3'
filters.timeout = 5
filters.ssl_verify = False #allows self-signed https certificate

conn = ApiConnect('https://localhost/', filters)