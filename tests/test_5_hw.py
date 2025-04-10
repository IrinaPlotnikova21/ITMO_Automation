
# from selenium import webdriver
#
# driver = webdriver.Chrome(
# driver.get('https://www.saucedemo.com/')

from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

def test_search():
    password = driver.find_element(By.ID, "password")
    user_name = driver.find_element(By.ID, "user-name")
    button = driver.find_element(By.ID, "login-button")

    if button is not None and user_name is not None and password is not None:
        print('Элементы найдены')
    else:
        print('Элемент не найден')


# поиск элемента
# def test_search_user_name():
#     user_name = driver.find_element(By.ID, "user-name")
#     if user_name is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')
#
# def test_search_password():
#     password = driver.find_element(By.ID, "password")
#     if password is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')
#
# def test_search_button():
#     button = driver.find_element(By.ID, "login-button")
#     if button is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')


