# video tutorial is located at: https://www.youtube.com/watch?v=qbLc5a9jdXo&t=1283s
# api is located at: https://api.stackexchange.com/

import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#print(response)
#print(response.json()['items'])
for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
        print(' ')
        print('-=-=-=-=-')
        print(' ')
    else:
        print('Too many answers!')
        print(' ')
        print('-=-=-=-=-')
        print(' ')