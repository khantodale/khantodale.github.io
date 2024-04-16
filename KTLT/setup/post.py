import requests
import read
def post():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 9e9d9a5558a7d381a4233907f0d8a4aec59fb4838ce35a8bf623460efd1d3e7c"
    }
    for i in range(1,11):
        res = requests.post("https://gorest.co.in/public/v2/posts",json=read.read_file(f"D:\\KTLT\\setup\\c{i}.json"),headers= headers)
        print(res.status_code)
        print(res.json())
post()