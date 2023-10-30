import requests
endpoint="http://127.0.0.1:8000/api/products/alldata/"

data={
    "title":"This field is done",
    "price":"32.99"
}
get_res=requests.get(endpoint)
print(get_res.json())