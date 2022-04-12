# Python program to read
# json file
# https://www.geeksforgeeks.org/read-json-file-using-python/
# https://stackoverflow.com/questions/10288752/reading-a-file-with-json-data-with-python-throw-an-error-that-i-cannot-identify/10289756

import json

# # Opening JSON file
# f = open("Output__2022-04-11_12_03_39-721381.json")

# # returns JSON object as
# # a dictionary
# data = json.load(f)

# # Iterating through the json
# # list
# for i in data['emp_details']:
# 	print(i)

# # Closing file
# f.close()

# ------

# give stream object
json_file = open('Output__2022-04-11_12_03_39-721381.json')
data = json.load(json_file)
json_file.close()

print(data)


#  # Opening JSON file
# with open('Output__2022-04-11_12_03_39-721381.json', 'r') as json_file:
#     data = json.load(json_file)

# # # Iterating through the json
# # # list
# for i in data['emp_details']:
#  	print(i)

# # # Closing file
# json_file.close()