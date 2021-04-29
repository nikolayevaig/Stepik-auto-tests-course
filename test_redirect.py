from selenium import webdriver
import time
import math

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    option1 = browser.find_element_by_css_selector('.trollface.btn').click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    option2 = browser.find_element_by_css_selector('.form-control').send_keys(y)
    option3 = browser.find_element_by_css_selector('.btn ').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()