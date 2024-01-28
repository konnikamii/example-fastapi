import pytest
from app import schemas
from jose import jwt
from app.config import settings


# def test_root(client):
#     res = client.get('/')
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hyyyy therere'
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "carlos@gmail.com", "password": "123"})
    new_user = schemas.UserOut(**res.json())
    assert res.json().get("email") == "carlos@gmail.com"
    assert res.status_code == 201


def test_login_user(client, create_test_user):
    res = client.post(
        "/login", data={"username": create_test_user['email'], "password": create_test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get('user_id')
    assert id == create_test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', '123', 403),
    ("carlos@gmail.com", 'wrong123', 403),
    ('wrongemail@gmail.com', 'wrong123', 403),
    (None, '123', 422),
    ("carlos@gmail.com", None, 422),
])
def test_incorrect_login(client, create_test_user, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'
