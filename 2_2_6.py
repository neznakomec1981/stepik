from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try:
    def func(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = func(int(x))
    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)



    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    browser.find_element(By.ID, "robotsRule").click()

    # Отправляем заполненную форму

    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    #browser.quit()

