import pytest
import requests

from duckduckrest.duck_duck_rest import list_of_presidents

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents+of+united+states&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]
