# video this is based off of: https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM
# graphing data in python: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

''' Javascript Object notation'''
import json
from urllib.request import urlopen

# ------------------------------------------------
# 192.168.50.190
# https://192.168.50.190/esmond/perfsonar/archive/
# ------------------------------------------------
# read data from local ip of perfsonar server REST API -> store into source variable
with urlopen("http://192.168.50.190/esmond/perfsonar/archive/") as response:
    source = response.read()

# take source data, load as json and move to data var
data = json.loads(source)

# add formatting
print(json.dumps(data, indent=2))


for item in data:
    # will print originating perfsonar node for the item
    print(item['input-destination'])

    # will print the unique uri for the originating perfsonar node
    print(item['metadata-key'])

    # print space seperator
    print(' ')
    print('-=-=-=-=-=-=-=-=-=-=-=-')
    print(' ')


# create and write out server data 

with open('My_Perfsonar_Server_jake_sorted_2.json', 'w') as z:
    json.dump(data, z, indent=2,sort_keys=True)
''''''

## THIS is how you grab data from the api, format it as a json and then output it with the correct info


## NOTE: remember to add the date function to dynamically name json outputs


