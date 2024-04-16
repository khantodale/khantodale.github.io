import json
def get_base_url():
    #lay url tu base.json
    with open("D:\\KTLT\\base.json","r") as json_file:
        properties = json.load(json_file)
        env = properties["environment"]["env"]
        return properties[env]["base_url"]