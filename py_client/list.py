import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter your username.\n")
password = getpass("Enter your password.\n")

auth_resp = requests.post(auth_endpoint, json={'username':'gbeng',
 'password': password})
print(auth_resp.json())

if auth_resp.status_code == 200:
    token = auth_resp.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://localhost:8000/api/products/"

    get_resp = requests.get(endpoint, headers=headers)
    print(get_resp.json())