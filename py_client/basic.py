import requests
endpoint="http://127.0.0.1:8000/api/1/"

get_res=requests.post(endpoint,params={"abc":123},json={"titl":"hello world"})
print(get_res.json())