from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #def calc(x):
    #    return str(math.log(abs(12*math.sin(int(x)))))  
    #img = browser.find_element_by_id("treasure")

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = x_element.text
    y = y_element.text
    z = str(int(x) + int(y))
    print(z)
    
    
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) # ищем элемент с текстом "Python"

 
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()