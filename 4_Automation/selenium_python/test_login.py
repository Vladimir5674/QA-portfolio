from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # Ввод логина и пароля
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Проверка успешного входа
    assert "inventory.html" in driver.current_url, "Login failed!"

    driver.quit()


def test_empty_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "login-button").click()

    # Проверка сообщения об ошибке
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Password is required" in error_message, "Error message not displayed"

    driver.quit()
