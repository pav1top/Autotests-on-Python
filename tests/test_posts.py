import pytest

def test_get_post_by_id_returns_200(api, base_url):
    response = api.get(f"{base_url}/posts/1")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id_matches_requested_id(post_id, api, base_url):
    response = api.get(f"{base_url}/posts/{post_id}")

    assert response.status_code ==  200
    
    body = response.json()
    assert body["id"] == post_id
