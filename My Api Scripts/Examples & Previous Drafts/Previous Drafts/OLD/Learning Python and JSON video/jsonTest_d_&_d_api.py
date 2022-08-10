# https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM

''' Javascript Object notation'''
import json
from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

with urlopen("https://www.dnd5eapi.co/api/spells/acid-arrow") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

with open('D_&_D_jake_sorted.json', 'w') as z:
    json.dump(data, z, indent=2,sort_keys=True)

## THIS is how you grab data from the api, format it as a json and then output it with the correct info
'''   
outputSource = source.decode("utf-8")

with open('D_&_D_jake.json', 'w') as z:
    json.dump(outputSource, z, indent=2)
    ''' 

