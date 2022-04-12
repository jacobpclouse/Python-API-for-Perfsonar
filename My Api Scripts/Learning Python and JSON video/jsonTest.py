# https://www.youtube.com/watch?v=9N6a-VLBa2I
# encoder for json in python docs: https://docs.python.org/3/library/json.html

''' Javascript Object notation'''
import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# use this to load json data into python dic
data = json.loads(people_string)


# printing out data and info
print(f"The type of the JSON file is: {type(data)}")
print(data)

print('    ')
for person in data['people']:
    del person['phone']

#    print(person['name'])

# indents will format each new item with n number of indents (ie: 2 in this case)
# sort keys will sort each attribute of the item alphabetically 
new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)