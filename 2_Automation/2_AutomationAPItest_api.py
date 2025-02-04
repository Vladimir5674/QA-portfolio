import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page(browser):  # Используем параметризацию браузеров
    page = browser.new_page()
    yield page
    page.close()


def test_checkout_flow(page: Page):
    # Авторизация
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Добавление товара в корзину
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")

    # Проверка корзины
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    page.click("#checkout")

    # Заполнение данных
    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")
    page.click("#continue")

    # Проверка итогов
    expect(page.get_by_text("Payment Information")).to_be_visible()
    page.click("#finish")
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
