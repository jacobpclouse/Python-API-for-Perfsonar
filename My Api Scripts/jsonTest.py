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

for person in data['people']:
    print(person['name'])