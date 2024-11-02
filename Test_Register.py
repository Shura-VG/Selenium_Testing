# http://127.0.0.1:8000
# pytest Test_Register.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_register(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[11]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[2]/input").send_keys("shura@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/input").send_keys("0777696969")
    driver.find_element(By.ID, "password").send_keys("222333444")
    driver.find_element(By.ID, "password_confirmation").send_keys("222333444")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[6]/button").click()
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("shura@gmail.com")
    driver.find_element(By.ID, "password").send_keys("222333444")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(2)
    user_name = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").text
    assert "Shura" in user_name

def test_existing_email(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[11]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[2]/input").send_keys("shura@gmail.com")
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/input").send_keys("0777696969")
    driver.find_element(By.ID, "password").send_keys("222333444")
    driver.find_element(By.ID, "password_confirmation").send_keys("222333444")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[6]/button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div").text
    assert "×\nOpps ! Email already registered !" in error_message

def test_mismatched_passwords(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[11]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("222333444")
    driver.find_element(By.ID, "password_confirmation").send_keys("69696969")
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[2]/input").send_keys("shura2@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/input").send_keys("0777667788")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[6]/button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div").text
    assert "×\nOpps ! Password do not match !" in error_message

def test_required_fields_left_blank(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[11]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[6]/button").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/register", "Form was submitted despite missing required fields"


def test_invalid_email_format(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[11]/a").click()
    time.sleep(1)
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[2]/input")
    email_field.send_keys("invalidgmail.com")
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/input").send_keys("0777696969")
    driver.find_element(By.ID, "password").send_keys("222333444")
    driver.find_element(By.ID, "password_confirmation").send_keys("222333444")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[6]/button").click()
    time.sleep(2)
    email_field.send_keys(Keys.TAB)  
    validation_message = email_field.get_attribute("validationMessage")
    assert validation_message == "Please include an '@' in the email address. 'invalidgmail.com' is missing an '@'.", "Expected validation message not displayed"
    