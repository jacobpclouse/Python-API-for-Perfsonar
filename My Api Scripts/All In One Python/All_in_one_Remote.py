# *** MAIN PERFSONAR REST API DOCUMENTATION: https://docs.perfsonar.net/esmond_api_rest.html ***
# video this is based off of: https://www.youtube.com/watch?v=9N6a-VLBa2I

## Part 1:
# https://www.dataquest.io/blog/python-api-tutorial/
# https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
# https://docs.perfsonar.net/esmond_api_python.html
# Python Filters: https://www.programiz.com/python-programming/methods/built-in/filter

# Part 2:
# This will load all the files from the remote server and then output the name, url and meta key
# Remove unneeded fields in python: https://stackoverflow.com/questions/68374796/delete-unnecessary-elements-in-json
# Create JSON from dictionary: https://pythonexamples.org/python-create-json/
# how to skip an item if it is not in the json: https://stackoverflow.com/questions/62066527/python-skip-over-key-if-it-doesnt-exist-in-json-array
# add new keyvalue pairs to dictionary: https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/
# remove everything after a string in python: https://www.adamsmith.haus/python/answers/how-to-remove-everything-after-a-character-in-a-string-in-python

# Part 3:
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM
# graphing data in python: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# appending to file: https://www.geeksforgeeks.org/python-append-to-a-file/


'''
OVERVIEW OF PROGRAM FUNCTION:
This will take in the remote server IP from the command line
It will output a dictionary of the corresponding keys and the corresponding hostnames  (if they exist, it will check) as a JSON file to reference
It will then go through all the tests and grab individual tests based on nodes, ouputting them to their own JSON files (with checks to see if they exist)

'''

# ----------
# Imports:
# ----------

import json
from textwrap import indent
from urllib.request import urlopen
import datetime
import sys
from msilib.schema import Directory
import os


# ----------
# Variables:
# ----------

# count variable
count = 0

# empty dictionary to store source IP or sourcehostname
nameSourceIPDictionary = dict()


# Current Server Source IP
current_server_IP = '192.168.50.190'

### Vars for specific tests ###
# URI Throughput:           /esmond/perfsonar/archive/{meta_key}/throughput/base
# URI Delay/One-way Delay:  /esmond/perfsonar/archive/{meta_key}/histogram-rtt/base
# URI OWDelay Base:         /esmond/perfsonar/archive/{meta_key}/histogram-owdelay/base
# URI OWDelay Aggregation:  /esmond/perfsonar/archive/{meta_key}/histogram-owdelay/aggregations
# URI OWDelay Statistics:   /esmond/perfsonar/archive/{meta_key}/histogram-owdelay/statistics/0
# URI Packet Loss:          /esmond/perfsonar/archive/{meta_key}/packet-loss-rate/base
# URI Packet Traces:        /esmond/perfsonar/archive/{meta_key}/packet-trace/base
# URI Subinterval Data:     /esmond/perfsonar/archive/{meta_key}/packet-retransmits-subintervals/base

# Base URI to put before meta Key var
base_uri = '/esmond/perfsonar/archive/'

# Dictionary of all the test key and uri pairs to look at
test_data_URIs = {
    'Throughput_All':'/throughput/base',
    'Delay_All':'/histogram-rtt/base',
    'OWDelay_Base_All':'/histogram-owdelay/base',
#    'OWDelay_Aggregation_All':'/histogram-owdelay/aggregations',
#    'OWDelay_Statistics_All':'/histogram-owdelay/statistics',
    'Packet_Loss_All':'/packet-loss-rate/base',
    'Packet_Traces_All':'/packet-trace/base',
    'Subinterval_Data_All':'/packet-retransmits-subintervals/base'
}

# Current Request URI (ex: '/esmond/perfsonar/archive/' or '/esmond/perfsonar/archive/?event-type=throughput' )
#current_URI = f'{base_uri}{meta_key}/throughput/base'



# ----------
# Functions:
# ----------


# importing Command line arguments - for IP and port numbers
# https://cs.stanford.edu/people/nick/py/python-main.html

#  --- Function to get server you want from command line --- 
def returnRemoteServer():
    remoteIP = sys.argv[1]
    return remoteIP


# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f'_{datetime.datetime.now()}'

    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace(".","-")
    current_datetime = current_datetime.replace(" ","_")
    
    return current_datetime


#  --- Function to write out to file --- 
def writeOutToFile(outgoingData,currentDatetime,filenamePrefix):
    with open(f'{filenamePrefix}{currentDatetime}.json', 'a') as z:
        json.dump(outgoingData,z,indent=2)


#  --- Function to make folder --- 
# source: https://www.geeksforgeeks.org/create-a-directory-in-python/
def makeFolder(directory):
    
    # Parent Directory path
    parent_dir = "./"
    
    # Path
    path = os.path.join(parent_dir, directory)
    
    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("Directory '% s' created" % directory)
    
    return directory


#  --- Function to open URI and load data --- 
def openApiUri(sourced_server_IP,target_test_URI):
    # read data from local ip of perfsonar server REST API -> store into source variable
    with urlopen(f"http://{sourced_server_IP}{target_test_URI}") as response:
        outbound_source = response.read()

    # take source data, load as json and move to data var
    outbound_data = json.loads(outbound_source)

    return outbound_data


'''
MAIN
'''

# Grab current date & time from function & store in variable
use_this_datetime = defang_datetime()

# grab remote server from command line
remote_server_IP = returnRemoteServer()


### PREFIXES: 

# Current Prefix for this file (maybe prompt user to input custom perfix?)
FullJSONFilename = f"{remote_server_IP}_Full_Data___"

# Prefix for the Dictionary JSON
DictionaryJSONFilename = f'{remote_server_IP}_Host_Names_MetaData_Keys_'


# ------------------------------------------------
# example: 
# kv-core-ps1-v4.uran.net.ua
# 212.111.192.61
# https://kv-core-ps1-v4.uran.net.ua/esmond/perfsonar/archive/
# https://212.111.192.61/esmond/perfsonar/archive/
# ------------------------------------------------

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



### PART 1: Output Full API File to JSON

# read data from local ip of perfsonar server REST API -> store into source variable
with urlopen(f"http://{remote_server_IP}/esmond/perfsonar/archive/") as response:
    source = response.read()

# take source data, load as json and move to data var
data = json.loads(source)

# create and write out server data 
writeOutToFile(data,use_this_datetime,FullJSONFilename)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



### PART 2: Create a Dictionary of Metadata-keys as keys to Hostnames as values for test lookups later on

# loop through full JSON and locate metadata-keys and hostnames
for item in data:

    # setting default values for key/value pairs (in case it doesn't exist in testing)
    inputDestination = "null"
    metadataKey = "null"

    # checks to see if input destination is in item, will skip if not
    if 'input-destination' in item:
        # will print originating perfsonar node for the item
        inputDestination = item['input-destination']
        print(inputDestination)

    # checks to see if metadata-key is in item, will skip if not
    if 'metadata-key' in item:
        # will print the unique uri for the originating perfsonar node
        metadataKey = item['metadata-key']
        print(metadataKey)

    # print space seperator
    print(' ')
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    print(' ')


    # Update dictionary (metadata-key is the key : input-destination is the value)
    newAddition = {metadataKey : inputDestination}
    nameSourceIPDictionary.update(newAddition)
	
	# Incriment Count
    count = count + 1


# print out dictionary
print(nameSourceIPDictionary)

# print out number of items in data
print(f'There are {count} host(s) connected to the {remote_server_IP} node')


# load dictionary into json
writeOutToFile(nameSourceIPDictionary,use_this_datetime,DictionaryJSONFilename)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


### PART 3: Getting all the tests for each node

## make sure that the right key is getting selected


# Itterating through the dictionary to get all the data
for metaDataKey in nameSourceIPDictionary:

    # Make output folder name and create new directory to store json files
    newDirectory = f"_{metaDataKey}_{use_this_datetime}"
    makeFolder(newDirectory)

    # Itterating through all the test for each individual node
    for test in test_data_URIs:

        # Current Request URI (ex: '/esmond/perfsonar/archive/' or '/esmond/perfsonar/archive/?event-type=throughput' )
        current_URI = f'{base_uri}{metaDataKey}{test_data_URIs[test]}'   
        print(current_URI)

        print("-=-=-=-=-")
       

        # Current Prefix for this file
        current_server_prefix = f'{test}_{metaDataKey}_'


        # load data from api
        data = openApiUri(current_server_IP,current_URI)


        # write out to file - event types 
        writeOutToFile(data,use_this_datetime,current_server_prefix,newDirectory)

        # clear out uri
        current_URI = ''

