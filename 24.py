from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, когда цена станет $100 (ожидание до 15 секунд)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отправляем решение
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Копируем код из alert
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Код из alert:", alert_text.split()[-1])
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()