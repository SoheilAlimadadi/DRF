import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input('username: ')
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/products/"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    re = requests.get(endpoint, headers=headers)
    print(re.json())
else:
    print('oops')