import api_url
import get_header
import file
import requests
def test_post():
    url = api_url.get_url
    headers = get_header.get_header_url()
    c_u = file.read_file("D:\\KTLT\\create_test4.json")
    response = requests.post(url,json=c_u, headers=headers)
    print(response.status_code)
    if response.status_code == 201 :
        re_json = response.json()
        id = re_json["id"]
        print(re_json)
        print("API success")

test_post()
