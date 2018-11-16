import requests
import json

address = r""

def get_player_info():
    url = r"http://{}/up/world/world/".format(address)
    res = requests.get(url)
    return json.loads(res.text)

if __name__ == "__main__":
    print(get_player_info())
