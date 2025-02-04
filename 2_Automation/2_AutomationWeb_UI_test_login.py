from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login(browser):
    browser.get("https://www.saucedemo.com/")

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    assert "inventory" in browser.current_url
    assert browser.find_element(By.CLASS_NAME, "title").text == "Products"
