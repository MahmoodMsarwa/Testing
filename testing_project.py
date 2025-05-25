import random
import pytest
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = uc.Chrome()  # Using undetected_chromedriver

    elif browser == "edge":
        options = EdgeOptions()
        options.use_chromium = True
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()

def test_1(driver):

    sleep(3)

    E = driver.find_element(By.ID, 'user-name')
    E.send_keys('standard_user')

    E = driver.find_element(By.ID, 'password')
    E.send_keys('secret_sauce')

    sleep(1)

    E = driver.find_element(By.ID, 'login-button')
    E.click()

    sleep(3)





def test_2(driver):

    sleep(3)

    E = driver.find_element(By.ID, 'user-name')
    E.send_keys('standard_user')



