# API: application programming interface

import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/1'  # API endpoint

response = requests.get(url=api_url)
print(response.json())

for key, value in response.json().items():
    if key == 'completed':
        if value == False:
            print("The received response is not complete")
        else:
            print("The received response is complete")