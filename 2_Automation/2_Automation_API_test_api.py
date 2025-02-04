import requests
import pytest

BASE_URL = "https://www.saucedemo.com"


def test_login_api():
    response = requests.post(
        f"{BASE_URL}/login",
        data={"user-name": "standard_user", "password": "secret_sauce"},
        allow_redirects=False,
    )
    assert response.status_code == 302  # Редирект после успешного входа
    assert "sessionid" in response.cookies.get_dict()
