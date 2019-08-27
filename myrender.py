import json

def craft(title):
    with open('./static/json/craft.json', 'r') as f:
        json_dict = json.load(f)
    anime=[]
    anime.append(json_dict[title])
    return anime

