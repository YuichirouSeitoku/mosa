import json

def read_json(title,path):
    with open(path, 'r') as f:
        json_dict = json.load(f)
    anime=[]
    anime.append(json_dict[title])
    return anime

def read_json2(title,path):
    with open(path, 'r') as f:
        json_dict = json.load(f)
    return json_dict[title]