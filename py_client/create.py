import requests
endpoint = "http://localhost:8000/api/products/"
data = {
    'title': 'This is a title',
    'price': 99.00
}
re = requests.post(endpoint, json=data)
print(re.json())
print(re.text)