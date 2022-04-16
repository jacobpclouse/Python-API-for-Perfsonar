# video this is based off of: https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM
# graphing data in python: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/


''' Javascript Object notation'''
## THIS is how you grab data from the api, format it as a json and then output it with the correct info

import json
from urllib.request import urlopen
import datetime
# ----------
# Variables:
# ----------

# count variable
count = 0


# empty dictionary to store keys
nameMetaDataKeyDictionary = dict()

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


#function to write out to file
def writeOutToFile(outgoingData,currentDatetime):
    with open(f'My_Perfsonar_Key_Outputs{currentDatetime}.json', 'a') as z:
        json.dump(outgoingData,z,indent=2)



'''
MAIN
'''
# Grab current date & time from function & store in variable
use_this_datetime = defang_datetime()

# ------------------------------------------------
# 192.168.50.190
# https://192.168.50.190/esmond/perfsonar/archive/
# ------------------------------------------------
# read data from local ip of perfsonar server REST API -> store into source variable
##with urlopen("http://192.168.50.190/esmond/perfsonar/archive/01dc42b87a854227b2cb5b7380efd8c7/?format=json") as response:
with urlopen("http://192.168.50.190/esmond/perfsonar/archive/") as response:
    source = response.read()

# take source data, load as json and move to data var
data = json.loads(source)

# print out and add formatting
#print(json.dumps(data, indent=2))

'''
# grabbing name and key of data
for item in data:
    # will print originating perfsonar node for the item
    print(item['input-destination'])

    # will print the unique uri for the originating perfsonar node
    print(item['metadata-key'])

    # print space seperator
    print(' ')
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    print(' ')

    # incriment count
    count = count + 1
'''



for item in data:
    # incriment count
    count = count + 1

    # print out base uri
    print(item['event-types'])
    print(' ')

    # will print originating perfsonar node for the item
    origin = item['input-destination']

    # will print the unique uri for the originating perfsonar node
    metaDataKey = item['metadata-key']

    # adding values to dictionary, origin as key, metadatakey as value
    nameMetaDataKeyDictionary[origin] = metaDataKey

    # print out keys and pairs
    print(nameMetaDataKeyDictionary[origin])

# write out to file
writeOutToFile(nameMetaDataKeyDictionary,use_this_datetime)


# output count of all the total originating nodes
print(f"Total node count = {count}")

## NOTE: remember to add the date function to dynamically name json outputs


'''
# create and write out server data 
with open(f'My_Perfsonar_Key_Outputs{use_this_datetime}.json', 'a') as z:
    json.dump((origin,metaDataKey),z,indent=2)
'''