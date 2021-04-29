from selenium import webdriver
import time
import math

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # Считать значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    #Посчитать математическую функцию от x.
    y = calc(x)

    #Проскроллить страницу вниз.
    textarea = browser.find_element_by_css_selector(".form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)

    #Ввести ответ в текстовое поле.
    
    textarea.send_keys(y)

    #Выбрать checkbox "I'm the robot".
    option1 = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()

    #Переключить radiobutton "Robots rule!".
    option2 = browser.find_element_by_css_selector('[for="robotsRule"]').click()

    #Нажать на кнопку "Submit".
    button = browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(8)
    browser.quit()