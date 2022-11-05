import requests

product_id = input('Which product id you want to delete? ')
try: product_id = int(product_id)
except: print(f'{product_id} is not valid.')

endpoint = f"http://localhost:8000/api/products/1/delete/"

re = requests.delete(endpoint)
print(re.status_code, re.status_code == 204)