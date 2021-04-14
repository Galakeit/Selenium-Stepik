from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("Petrov")
    input2 = browser.find_element_by_name("firstname")
    input2.send_keys("Petrov")    
    input3 = browser.find_element_by_name("email")
    input3.send_keys("petrov@mail.ru")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("petrov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "download.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла