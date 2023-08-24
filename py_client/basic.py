import requests

endpoint = "http://localhost:8000/api/"

get_resp = requests.get(endpoint)
print(get_resp.json())
 

#  , json={"title":"Hello World", "content": "How are you doing?", "price": "88"}