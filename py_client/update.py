import requests
endpoint="http://127.0.0.1:8000/api/products/1/update/"

data={
    "title":"vignesh",
    "price":1.99
}
get_res=requests.put(endpoint,json=data)
print(get_res.json())