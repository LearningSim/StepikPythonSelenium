import os

import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


name = browser.find_element_by_css_selector('input[name="firstname"]')
name.send_keys('a')

surname = browser.find_element_by_css_selector('input[name="lastname"]')
surname.send_keys('a')

mail = browser.find_element_by_css_selector('input[name="email"]')
mail.send_keys('a')

file = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty.txt')
file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()
