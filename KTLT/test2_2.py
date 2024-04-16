import api_url
import get_header
import file
import requests


def test_get():
    url = api_url.get_url
    headers = get_header.get_header_url_test2_2()
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
        print("API success")
   

def test_post():
    url = api_url.get_url
    headers = get_header.get_header_url_test2_2()
    c_u = file.read_file("D:\\KTLT\\create.json")
    response = requests.post(url,json=c_u, headers=headers)
    print(response.status_code)
    if response.status_code == 201 :
        re_json = response.json()
        id = re_json["id"]
        print(re_json)
        print("API success")
        
    
def test_put():
    id = 118196
    url = api_url.get_url + f"/{id}"
    headers = get_header.get_header_url_test2_2()
    c_u = file.read_file("D:\\KTLT\\update.json")
    response = requests.put(url, json=c_u, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())
        print("API success")

def test_delete():
    id = 118196
    url = api_url.get_url + f"/{id}"
    headers = get_header.get_header_url_test2_2()
    response = requests.delete(url, headers=headers)
    print(response.status_code)
    if response.status_code == 204:
        print("Delete success")
    
def main():
    test_get()
    test_post()
    test_put()
    test_delete()
if __name__ == "__main__":
    main()
