from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

try:
    link = "http://suninjuly.github.io/registration%s.html"
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,900")
    chrome_options.add_argument("--user-data-dir=K:\\chrome_profiles\\qa_chrome")
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome('../bin/chromedriver96.exe', chrome_options=chrome_options)
    browser.get(link % 1)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//label[contains(text(), "First")]/following-sibling::input')
    input1.send_keys('First name')
    input2 = browser.find_element_by_xpath('//label[contains(text(), "Last")]/following-sibling::input')
    input2.send_keys('Last name')
    input3 = browser.find_element_by_xpath('//label[contains(text(), "Email")]/following-sibling::input')
    input3.send_keys('Email')

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
