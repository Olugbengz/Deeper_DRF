import requests

endpoint = "http://localhost:8000/api/products/2/update/"

data = {
    "title": "Getting clearer",
    "price": 96
}

get_resp = requests.put(endpoint, json=data)
print(get_resp.json())