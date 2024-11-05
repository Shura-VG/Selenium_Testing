# http://127.0.0.1:8000
# pytest Test_Login_Logout.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    assert "http://127.0.0.1:8000/redirects" in driver.current_url

def test_invalid_login(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("wrong@gmail.com")
    driver.find_element(By.ID, "password").send_keys("12345678")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div").text
    assert "Whoops! Something went wrong." in error_message

def test_logout(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/form/a").click()
    time.sleep(1)
    assert "http://127.0.0.1:8000" in driver.current_url