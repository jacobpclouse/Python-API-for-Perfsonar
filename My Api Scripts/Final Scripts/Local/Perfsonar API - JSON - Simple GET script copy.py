# video this is based off of: https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM
# graphing data in python: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# appending to file: https://www.geeksforgeeks.org/python-append-to-a-file/


''' Javascript Object notation

     _____ _                 _         _____ ______ _______ 
    / ____(_)               | |       / ____|  ____|__   __|
   | (___  _ _ __ ___  _ __ | | ___  | |  __| |__     | |   
    \___ \| | '_ ` _ \| '_ \| |/ _ \ | | |_ |  __|    | |   
    ____) | | | | | | | |_) | |  __/ | |__| | |____   | |   
   |_____/|_|_| |_| |_| .__/|_|\___|  \_____|______|  |_|   
                      | |                                   
                      |_|                                   
'''

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


# ----------
# Variables:
# ----------

# ------------------------------------------------
# 192.168.50.190
# https://192.168.50.190/esmond/perfsonar/archive/
# ------------------------------------------------
# Current Server IP
current_server_IP = '192.168.50.190'

# Current Prefix for this file (maybe prompt user to input custom perfix?)
current_server_prefix = "Local_Server__"


'''
MAIN
'''
# Grab current date & time from function & store in variable
use_this_datetime = defang_datetime()

# read data from local ip of perfsonar server REST API -> store into source variable
with urlopen(f"http://{current_server_IP}/esmond/perfsonar/archive/") as response:
    source = response.read()

# take source data, load as json and move to data var
data = json.loads(source)


# write out to file - event types 
writeOutToFile(data,use_this_datetime,current_server_prefix)



