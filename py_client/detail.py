import requests

endpoint = "http://localhost:8000/api/products/2/"

get_resp = requests.get(endpoint)
print(get_resp.json())



# params={"abs":123},
# json={"query":"Hello World"}