from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #def calc(x):
    #    return str(math.log(abs(12*math.sin(int(x)))))  
    #img = browser.find_element_by_id("treasure")

    def calc(x):
       return str(math.log(abs(12*math.sin(int(x)))))  
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    print(x)
    print(y)
   


    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    

    button.click()
  

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()