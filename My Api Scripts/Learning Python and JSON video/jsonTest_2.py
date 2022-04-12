# https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html
# working with objects in python: https://www.youtube.com/watch?v=Uh2ebFW8OYM

''' Javascript Object notation'''
import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    #print(state['name'], state['abbreviation'])
    del state['area_codes']


# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(f"New string loaded is: {new_string}")


with open('new_states_jake.json', 'w') as z:
    json.dump(data, z, indent=2)