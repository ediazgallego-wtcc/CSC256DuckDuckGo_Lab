import requests


def list_of_presidents():
    return "Esteban"


def main():
    url_ddg = "https://api.duckduckgo.com"
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    print("Hello")
    print(list_of_presidents())
    print(rsp_data)
