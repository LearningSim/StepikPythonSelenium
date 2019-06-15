from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# заполняем форму регистрации
input_name = browser.find_element_by_css_selector('.first_block .first')
input_name.send_keys("Софья")
input_lastname = browser.find_element_by_css_selector('.first_block .second')
input_lastname.send_keys("Ильиных")
input_email = browser.find_element_by_css_selector('.first_block .third')
input_email.send_keys("@gmail.com")
input_telephone = browser.find_element_by_css_selector('.second_block .first')
input_telephone.send_keys("1234567890")
input_adress = browser.find_element_by_css_selector('.second_block .second')
input_adress.send_keys("Санкт-Петербург")
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
time.sleep(1)
welcome_text = browser.find_element_by_tag_name('h1')
welcome_text.text
assert "Поздравляем" in welcome_text.text
browser.quit()
