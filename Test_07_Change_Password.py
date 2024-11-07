# http://127.0.0.1:8000
# pytest Test_Change_Password.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_password_changed(driver):
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
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "current_password").send_keys("69696969")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "password_confirmation").send_keys("123456789")
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[2]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/form/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    assert "http://127.0.0.1:8000/redirects" in driver.current_url

def test_incorrect_current_password(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "current_password").send_keys("69696969")
    driver.find_element(By.ID, "password").send_keys("12345678")
    driver.find_element(By.ID, "password_confirmation").send_keys("12345678")
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[2]/button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[1]/div/div[1]/p").text
    assert "The provided password does not match your current password." in error_message

def test_password_do_not_match(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "current_password").send_keys("123456789")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.ID, "password_confirmation").send_keys("12345678")
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[2]/button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[1]/div/div[2]/p").text
    assert "The password confirmation does not match." in error_message

def test_invalid__new_password(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "current_password").send_keys("123456789")
    driver.find_element(By.ID, "password").send_keys("6969")
    driver.find_element(By.ID, "password_confirmation").send_keys("6969")
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[2]/button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[1]/div/div[2]/p").text
    assert "The password must be at least 8 characters." in error_message

def test_empty_fields(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[2]/button").click()
    time.sleep(2)
    error_message_1 = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[1]/div/div[1]/p").text
    assert "The current password field is required." in error_message_1
    error_message_2 = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/div[2]/form/div[1]/div/div[2]/p").text
    assert "The password field is required." in error_message_2