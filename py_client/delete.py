import requests

product_id = input("Type in your product ID\n")

try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not a valid product!')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_resp = requests.delete(endpoint)
    print(get_resp.status_code, get_resp.status_code==204)