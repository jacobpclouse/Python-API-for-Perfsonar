'''
Python API project

all extensions:
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

'''
# ----------
# Imports:
# ----------
import json
from urllib.request import urlopen
import datetime


# ----------
# Variables:
# ----------

# Test uri - only using one
singleMetaKey = [
    "f967831a91d548369d4c1af50789c048"
]


# these are all the uris of the data nodes
dataMetaKeys = [
    "f967831a91d548369d4c1af50789c048",
    "f4944621ceff4e76905d28f6f5e77925",
    "f8dc2b4440b6424bb1eb4d4d8d2e9646",
    "82db14fd564b46cab9d4600c7126309e",
    "a794af635b7740baa8ea0f0beabe67d1",
    "df598b50ca064ff9bcb425a4cb7d3cce",
    "917d0bf8d55649aa894e118d8233d54f",
    "80eb51ab534d43c8b19d6aa1d70026be",
    "d5da4cf79d1a4b798d19b49052a7b1a4",
    "d8e1ea7e2f96402199689e67c3e42c63"
    ]

# count variable
count = 0

# -- URI paths --

# prefix - failures 
failuesPrefix = "failures_"
# uri - failures base
failuresURI = "/failures/base"


# prefix - packet trace
packetTracePrefix = "packet_trace_"
# uri - packet trace base
packetTraceURI = "/packet-trace/base"


# prefix - path-mtu
pathMtuPrefix = "path_mtu_"
# uri - path-mtu base
pathMtuURI = "/path-mtu/base"


# prefix - pscheduler
pschedulerPrefix = "pscheduler_"
# uri - pscheduler base
pschedulerURI = "/pscheduler-run-href/base"


# prefix - pscheduler - FULL
pschedulerPrefixFULL = "pscheduler_FULL_"
# uri - path-mtu base
pschedulerURIFULL = "/pscheduler-run-href"


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
        # print(',',end = '')


# use key to open api uri - can use any uri var above
def openApiUri(inputKey,specifiedURI):
    # read data from local ip of perfsonar server REST API -> store into source variable
    #with urlopen(f"http://192.168.50.190/esmond/perfsonar/archive/{inputKey}/packet-trace/base") as response:
    with urlopen(f"http://192.168.50.190/esmond/perfsonar/archive/{inputKey}{specifiedURI}") as response:
        OutSource = response.read()
        # take source data, load as json and move to data var
        Outdata = json.loads(OutSource)
        return Outdata

'''
MAIN 
*** need four of these source pulls, one for each of the attributes, then plot them and store them (or vise versa)
- get it so that you can specifiy the you only want one url - new var - seperate jsons
'''
# Grab current date & time from function & store in variable
use_this_datetime = defang_datetime()

# itterate through loop of keys
#for keys in dataMetaKeys:
for keys in singleMetaKey:

    # incriment count
    count = count + 1

    # grab key
    print(keys)
    # insert it into url for api
    #print(f'http://192.168.50.190/esmond/perfsonar/archive/{keys}/packet-trace/base')
    print(f'http://192.168.50.190/esmond/perfsonar/archive/{keys}{pschedulerURIFULL}')

    # getting data from uri - packet trace
    data = openApiUri(keys,pschedulerURIFULL)


    print(json.dumps(data, indent=2))

    print(' ')
    print(' ')
    print(' ')
    print("-=-=-=-=-=-=-=-")
    print(' ')
    print(' ')
    print(' ')


# ----

    # now storing data
    # write out to file - keys 
    writeOutToFile(data,use_this_datetime,pschedulerPrefixFULL)
