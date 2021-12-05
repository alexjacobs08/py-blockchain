from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_mine():
    response = client.get("/mine")
    assert response.status_code == 200
    assert response.json()[0]['index'] == 2
    return response

# def test_transaction():
#     response = test_mine()
#     sender = response.json()[0]['transactions'][0]['recipient']
#     print(sender)
#     payload = {
#             "sender": sender,
#             "recipient": "other-address",
#             "amount": 5
#     }
#     print(payload)
#
#     response = client.get("transactions/new", json=payload)
#     assert response.status_code == 200