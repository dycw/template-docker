from beartype import beartype
from fastapi.testclient import TestClient
from hypothesis import given
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from tests.strategies import clients


@given(client=clients())
@beartype
def test_root_endpoint(client: TestClient) -> None:
    r = client.get("/")
    assert r.status_code == HTTP_200_OK


@given(client=clients())
@beartype
def test_read_item(client: TestClient) -> None:
    r = client.get("/items/1", params={"q": "query"})
    assert r.status_code == HTTP_200_OK, r.text
    assert r.json()["item_id"] == 1


@given(client=clients())
@beartype
def test_update_item(client: TestClient) -> None:
    data = {"name": "New Item", "price": "0.38", "is_offer": True}
    r = client.put("/items/1", json=data)
    assert r.status_code == HTTP_200_OK, r.text
    assert r.json()["item_name"] == data["name"]


#


@given(client=clients())
@beartype
def test_root(client: TestClient) -> None:
    r = client.get("/users")
    assert r.status_code == HTTP_200_OK, r.text
    assert r.json() == []


@given(client=clients())
@beartype
def test_create(client: TestClient) -> None:
    data = {"email": "d.wan@icloud.com", "password": "password"}
    r = client.post("/users/create", json=data)
    assert r.status_code == HTTP_201_CREATED, r.text
    assert set(r.json()) == {"email"}
