import requests
endpoint = "http://localhost:8000/api/products/1/"
re = requests.get(endpoint)
print(re.json())
print(re.text)