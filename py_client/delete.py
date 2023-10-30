import requests

id=input("ENter product id\n")
try:
    id=int(id)
except:
    id=None
    print(f'{id} not a valid id')
if id:
    endpoint=f"http://127.0.0.1:8000/api/products/{id}/delete/"
    get_res=requests.delete(endpoint)
    print(get_res.status_code,get_res.status_code==204)