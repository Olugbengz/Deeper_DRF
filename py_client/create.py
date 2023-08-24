import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Learning DRF is fun."
}

get_resp = requests.post(endpoint, json=data)
print(get_resp.json())