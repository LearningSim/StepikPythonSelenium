import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

a_element = browser.find_element_by_id('num1')
a = int(a_element.text)
b_element = browser.find_element_by_id('num2')
b = int(b_element.text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(a + b))

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()
