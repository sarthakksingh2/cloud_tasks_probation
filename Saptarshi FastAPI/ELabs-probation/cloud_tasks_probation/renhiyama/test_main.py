from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_post():
    response = client.post("/posts/1?title=First post")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "post": {
        "id": 1, "title": "First post"}}

    response = client.post("/posts/1?title=First post")
    assert response.status_code == 200
    assert response.json() == {"status": "error"}


def test_read_post():
    response = client.get("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "First post"}

    response = client.get("/posts/2")
    assert response.status_code == 200
    assert response.json() == {"error": "Post not found"}


def test_read_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "First post"}]


def test_delete_post():
    response = client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

    response = client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"status": "error", "message": "Post not found"}

    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == []