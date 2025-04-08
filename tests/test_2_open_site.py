from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/')

def test_search_icon():
    icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
    if icon is None:
        print('Эдемент не найден')
    else:
        print('Элемент найден')