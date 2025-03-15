import requests


def test_login_api():
    url = "https://www.saucedemo.com/api/login"
    data = {"username": "standard_user", "password": "secret_sauce"}
    response = requests.post(url, json=data)

    assert (
        response.status_code == 200
    ), f"Ожидался код 200, получен {response.status_code}"
    assert "session_id" in response.cookies, "Сессия не создана"


def test_get_products():
    url = "https://www.saucedemo.com/api/products"
    response = requests.get(url)

    assert response.status_code == 200
    assert len(response.json()["items"]) == 6, "Некорректное количество товаров"
