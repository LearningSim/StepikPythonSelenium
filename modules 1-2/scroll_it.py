import math
from selenium import webdriver
import time

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

answer_input = browser.find_element_by_id('answer')
browser.execute_script("arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)

checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()

robots_rule = browser.find_element_by_css_selector("[for='robotsRule']")
robots_rule.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()
