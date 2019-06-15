from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


def fill_in_form():
    name = browser.find_element_by_css_selector('.first[required]')
    name.send_keys("Ivan")
    surname = browser.find_element_by_css_selector('.second[required]')
    surname.send_keys("Petrov")
    email = browser.find_element_by_css_selector('.third[required]')
    email.send_keys("a@mail.ru")


fill_in_form()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

time.sleep(5)
browser.quit()
