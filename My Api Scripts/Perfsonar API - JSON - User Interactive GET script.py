# video this is based off of: https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM
# graphing data in python: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# appending to file: https://www.geeksforgeeks.org/python-append-to-a-file/


''' Javascript Object notation '''
outside_nodes = {
  "kv-core-ps1-v4.uran.net.ua": "f967831a91d548369d4c1af50789c048",
  "kharkiv-ps.uran.net.ua": "f4944621ceff4e76905d28f6f5e77925",
  "perfsonar.reuna.cl": "f8dc2b4440b6424bb1eb4d4d8d2e9646",
  "dps10.ucsc.edu": "82db14fd564b46cab9d4600c7126309e",
  "ps.wan.noc.rabat.marwan.ma": "a794af635b7740baa8ea0f0beabe67d1",
  "cloud.prjinr.fmi.uni-sofia.bg": "df598b50ca064ff9bcb425a4cb7d3cce",
  "kherson-ps.uran.net.ua": "917d0bf8d55649aa894e118d8233d54f",
  "dnipro-ps.uran.net.ua": "80eb51ab534d43c8b19d6aa1d70026be",
  "vm-118-138-254-213.erc.monash.edu.au": "d5da4cf79d1a4b798d19b49052a7b1a4",
  "perfsonar.physics.science.az": "d8e1ea7e2f96402199689e67c3e42c63"
}


# ----------
# Import Libs:
# ----------

import json
from urllib.request import urlopen
import datetime

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


# Function to open URI and load data 
def openApiUri(sourced_server_IP,target_test_URI):
    # read data from local ip of perfsonar server REST API -> store into source variable
    with urlopen(f"http://{sourced_server_IP}{target_test_URI}") as response:
        outbound_source = response.read()

    # take source data, load as json and move to data var
    outbound_data = json.loads(outbound_source)

    return outbound_data


# ----------
# Variables:
# ----------

# Current Outside Node being queried (using meta key)
meta_key= outside_nodes["perfsonar.physics.science.az"]

# Current Server Source IP
current_server_IP = '192.168.50.190'


# Current Request URI (ex: '/esmond/perfsonar/archive/' or '/esmond/perfsonar/archive/?event-type=throughput' )
current_URI = f'/esmond/perfsonar/archive/{meta_key}/throughput/base'
# URI Throughput:           /esmond/perfsonar/archive/{meta_key}/throughput/base
# URI Delay/One-way Delay:  /esmond/perfsonar/archive/{meta_key}/histogram-rtt/base
#                           /esmond/perfsonar/archive/{meta_key}/histogram-owdelay/base
# URI Packet Loss:          /esmond/perfsonar/archive/{meta_key}/
# URI Packet Traces:        /esmond/perfsonar/archive/{meta_key}/
# URISubinterval Data:      /esmond/perfsonar/archive/{meta_key}/





'''
MAIN
'''

for key in outside_nodes:
    
    # Current Prefix for this file
    current_server_prefix = f'{key}_'


'''
# Grab current date & time from function & store in variable
use_this_datetime = defang_datetime()


# load data from api
data = openApiUri(current_server_IP,current_URI)


# write out to file - event types 
writeOutToFile(data,use_this_datetime,current_server_prefix)
'''