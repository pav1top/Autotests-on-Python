import requests
import pytest

def test_get_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    body = response.json()
    assert response.status_code == 200
    assert body["id"] == 1
