# This will load all the files from the remote server and then output the name, url and meta key
# Remove unneeded fields in python: https://stackoverflow.com/questions/68374796/delete-unnecessary-elements-in-json
# Create JSON from dictionary: https://pythonexamples.org/python-create-json/
# how to skip an item if it is not in the json: https://stackoverflow.com/questions/62066527/python-skip-over-key-if-it-doesnt-exist-in-json-array
# add new keyvalue pairs to dictionary: https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/
# remove everything after a string in python: https://www.adamsmith.haus/python/answers/how-to-remove-everything-after-a-character-in-a-string-in-python

# Imports
import json
from textwrap import indent
from urllib.request import urlopen
import datetime
import sys

# ----------
# Variables:
# ----------

# count variable
count = 0


# empty dictionary to store source IP or sourcehostname
nameSourceIPDictionary = dict()

# # empty dictionary to store keys
# nameMetaDataKeyDictionary = dict()

# # empty dictionary to store event types
# nameEventTypeDictionary = dict()

# ----------
# Functions:
# ----------


# importing Command line arguments - for IP and port numbers
# https://cs.stanford.edu/people/nick/py/python-main.html

# server you want to get data from - command line
def JSONFileNameFunc():
    JSONFileName = sys.argv[1]
    return JSONFileName


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
# get current date/time
currentDateTime = defang_datetime()


# store target JSON file
openJSON = JSONFileNameFunc()

# Open JSON File
JSONtoRead = open(openJSON)
JSONtoString = JSONtoRead.read()
data = json.loads(JSONtoString)

# store incomming url, trim to get output name
incomingUrl = data[0]['url']
# removing ending uri, replacing with underscore to split on later
incomingUrl = incomingUrl.replace("/esmond/perfsonar/archive/","_")
# removing http at start
incomingUrl = incomingUrl.replace("http://","")
# splitting string on udnerscore
split_string = incomingUrl.split("_", 1)
# taking first part os split string and moveing to new prefix
newPrefix = split_string[0]
print(newPrefix)

# Event type filename prefix
prefixFilename = f'Host_Names_MetaData_Keys_for_{newPrefix}'


# loop through and print things

for item in data:
    # setting default values for key/value pairs
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


    # Update dictionary
    newAddition = {inputDestination: metadataKey}
    nameSourceIPDictionary.update(newAddition)

# print out dictionary
print(nameSourceIPDictionary)


# load dictionary into json
writeOutToFile(nameSourceIPDictionary,currentDateTime,prefixFilename)
''''''