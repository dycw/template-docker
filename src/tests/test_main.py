from beartype import beartype
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_201_CREATED


@beartype
def test_root_endpoint(test_client: TestClient) -> None:
    r = test_client.get("/")
    assert r.status_code == HTTP_200_OK


@beartype
def test_read_item(test_client: TestClient) -> None:
    r = test_client.get("/items/1", params={"q": "query"})
    assert r.status_code == HTTP_200_OK, r.text
    assert r.json()["item_id"] == 1


@beartype
def test_update_item(test_client: TestClient) -> None:
    data = {"name": "New Item", "price": "0.38", "is_offer": True}
    r = test_client.put("/items/1", json=data)
    assert r.status_code == HTTP_200_OK, r.text
    assert r.json()["item_name"] == data["name"]


#


@beartype
def test_root(test_client: TestClient) -> None:
    r = test_client.get("/users")
    assert r.status_code == HTTP_200_OK, r.text
    assert r.json() == []


@beartype
def test_create(test_client: TestClient) -> None:
    data = {"email": "d.wan@icloud.com", "password": "password"}
    r = test_client.post("/users/create", json=data)
    assert r.status_code == HTTP_201_CREATED, r.text
    assert set(r.json()) == {"email"}
