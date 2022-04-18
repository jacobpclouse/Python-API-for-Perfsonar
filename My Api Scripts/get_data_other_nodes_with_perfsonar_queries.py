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

## GRAB FROM UKRAINE NODES - THEIR DATA, NOT JUST LOCAL SERVER

import json
from urllib.request import urlopen
import datetime
# ----------
# Variables:
# ----------

# count variable
count = 0

# Regular Json filename prefix
myPersonarKeyFilename = 'My_Perfsonar_Key_Outputs'

# Event type filename prefix
eventTypeFilename = 'Event_types_keys'

# empty dictionary to store keys
nameMetaDataKeyDictionary = dict()

# empty dictionary to store event types
nameEventTypeDictionary = dict()

# ----------
# Functions:
# ----------

# --- Defang date time ---
def defang_datetime():
    current_datetime = f'_{datetime.datetime.now()}'

    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace(".","-")
    current_datetime = current_datetime.replace(" ","_")
    
    return current_datetime


# function to write out to file
def writeOutToFile(outgoingData,currentDatetime,filenamePrefix):
    with open(f'{filenamePrefix}{currentDatetime}.json', 'a') as z:
        json.dump(outgoingData,z,indent=2)



'''
MAIN
'''
# Grab current date & time from function & store in variable
use_this_datetime = defang_datetime()


# Current Prefix for this file (maybe prompt user to input custom perfix?)
current_server_prefix = "REMOTE_SERVER_kv-core-ps1-v4_uran_net_ua__"

# ------------------------------------------------
# kv-core-ps1-v4.uran.net.ua
# 212.111.192.61
# https://kv-core-ps1-v4.uran.net.ua/esmond/perfsonar/archive/
# https://212.111.192.61/esmond/perfsonar/archive/
# ------------------------------------------------
# read data from local ip of perfsonar server REST API -> store into source variable
with urlopen("http://kv-core-ps1-v4.uran.net.ua/esmond/perfsonar/archive/") as response:
    source = response.read()


# take source data, load as json and move to data var
data = json.loads(source)


# print out to console
print(json.dumps(data, indent=2))


# create and write out server data 
writeOutToFile(data,use_this_datetime,current_server_prefix)

