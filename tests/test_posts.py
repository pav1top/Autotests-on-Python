import requests

def test_get_post_by_id_returns_200(base_url):
    response = requests.get(f"{base_url}/posts/1")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
