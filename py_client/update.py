import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': 'Hello world',
    'price': 125.95
}

re = requests.put(endpoint, json=data)
print(re.json())
print(re.status_code)