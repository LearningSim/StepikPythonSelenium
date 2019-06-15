import time

import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
)

book = browser.find_element_by_id("book")
book.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(answer)

solve = browser.find_element_by_id("solve")
solve.click()

time.sleep(5)
browser.quit()
