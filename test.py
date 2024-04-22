import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

browser = webdriver.Chrome()

browser.get('https://ru.pinterest.com/login/')

time.sleep(5)

# Вводим ваш email и пароль
email = browser.find_element(By.NAME, 'id')
email.send_keys('narekazaryan2004@gmail.com')  

password = browser.find_element(By.NAME, 'password')
password.send_keys('nkazaryan11')  

password.submit()
time.sleep(8)

browser.get('https://ru.pinterest.com/nkazaryan11/')
browser.get('https://ru.pinterest.com/nkazaryan11/аesthetics/')
time.sleep(5)

for i in range(3): 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

browser.get('https://ru.pinterest.com/pin/694398836325233416/')

time.sleep(3)

# Проверка результата
try:
    # Проверка заголовка страницы пина
    assert "Anatomical Heart Ceramic Vase" in browser.title
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')


# Закрываем браузер после выполнения операций
browser.quit()

