
import file
import get_header
import api_url
import os
import requests
def read_and_list_post():
    arr=[]
    folder_path = 'D:\\KTLT\\file_post'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            arr.append(file.read_file(file_path))
    return arr

def post(n):
    url = api_url.get_url
    headers = get_header.get_header_url()
    c_u = n
    response = requests.post(url,json=c_u, headers=headers)
    print(response.status_code)
    re_json = response.json()
    print(re_json)
    print("API success")

def test_post():
    for i in read_and_list_post():
        post(i)

def post_id():
    url = api_url.get_url
    headers = get_header.get_header_url()
    c_u = file.read_file("D:\\KTLT\\create.json")
    response = requests.post(url,json=c_u, headers=headers)
    if response.status_code == 201 :
        re_json = response.json()
        print(re_json)
        id = re_json["id"]
        return id

def put(n, id):
    url = api_url.get_url + f"/{id}"
    headers = get_header.get_header_url()
    c_u = n
    response = requests.put(url, json=c_u, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
        print("API success")

def test_put():
    id = post_id()
    for i in read_and_list_put():
        put(i, id)

def read_and_list_put():
    arr=[]
    folder_path = 'D:\\KTLT\\file_put'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            arr.append(file.read_file(file_path))
    return arr

test_put()

