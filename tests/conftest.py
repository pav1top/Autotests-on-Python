import pytest
import requests

@pytest.fixture
def base_url():
    base_url = "https://jsonplaceholder.typicode.com"
    return base_url
