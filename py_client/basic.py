import requests

endpoint = 'http://127.0.0.1:8000/api/'
response = requests.post(endpoint, json={'title': 'headphone', 'content': 'gaming', 'price': 129.9})
print(response.status_code)
print(response.text)