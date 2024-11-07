# http://127.0.0.1:8000
# pytest Test_Trace_Order.py

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

def test_valid_trace_order(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a").click()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("dlcjgy5t")
    driver.find_element(By.ID, "phone").send_keys("0706777124")
    time.sleep(2)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    assert "http://127.0.0.1:8000/trace/confirm" in driver.current_url

def test_invalid_invoice_number(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a").click()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("invalid")
    driver.find_element(By.ID, "phone").send_keys("0706777124")
    time.sleep(2)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div").text
    assert "×\nOpps ! Invaild Invoice no !" in error_message

def test_invalid_phone_number(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a").click()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("dlcjgy5t")
    driver.find_element(By.ID, "phone").send_keys("123456789")
    time.sleep(2)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div").text
    assert "×\nOpps ! Wrong phone no !" in error_message

def test_invalid_invoice_and_phone_number(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a").click()
    time.sleep(2)
    driver.find_element(By.ID, "name").send_keys("invalid")
    driver.find_element(By.ID, "phone").send_keys("123456789")
    time.sleep(2)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div").text
    assert "×\nOpps ! Invaild Invoice no !" in error_message

def test_empty_fields(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a").click()
    time.sleep(2) 
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    assert "http://127.0.0.1:8000/trace-my-order" in driver.current_url