import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
answer = calc(x)

answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(answer)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

robots_rule = browser.find_element_by_id("robotsRule")
robots_rule.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()
