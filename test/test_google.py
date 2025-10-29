import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_google(driver):
    driver = webdriver.Chrome()  # Открываем браузер Chrome
    driver.get("https://www.google.com")  # Переходим на страницу Google

    search_box = driver.find_element(By.NAME, "q")  # Находим поле поиска по имени
    search_box.send_keys("QA Automation")  # Вводим запрос
    search_box.submit()  # Отправляем форму (нажимаем Enter)

    time.sleep(10)  # Время ожидания загрузки страницы
    assert (
        "q=QA+Automation" in driver.current_url
        or "q=QA%20Automation" in driver.current_url
    )  # Проверяем URL
