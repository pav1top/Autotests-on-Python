import pytest
import requests

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers.update({"Accept" : "application/json"})
    yield session
    session.close()