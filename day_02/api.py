# API: application programming interface

import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url=url)
print(response.json())