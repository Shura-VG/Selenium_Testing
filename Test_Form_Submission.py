# http://127.0.0.1:8000
# pytest Test_Form_Submission.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_table_reservation(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[7]/a").click()
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.ID, "email").send_keys("shura@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("0706696969")
    # Random guest
    dropdown_guest = Select(driver.find_element(By.ID, "number-guests"))
    options = dropdown_guest.options
    random_guest = random.choice(options[1:])  # Skip the first option which is usually a placeholder
    dropdown_guest.select_by_visible_text(random_guest.text)
    time.sleep(1)
    driver.find_element(By.ID, "date").send_keys("24/03/2025")
    # Random time
    dropdown_time = Select(driver.find_element(By.ID, "time"))
    options = dropdown_time.options
    random_time = random.choice(options[1:])  # Skip the first option which is usually a placeholder
    dropdown_time.select_by_visible_text(random_time.text)
    time.sleep(1)
    driver.find_element(By.ID, "message").send_keys("Random message")
    time.sleep(3)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(3)
    message = driver.find_element(By.XPATH,"/html/body/div/h1").text
    assert "Success" in message

def test_invalid_email(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[7]/a").click()
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.ID, "email").send_keys("invalidgmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "phone").send_keys("0706696969")
    # Random guest
    dropdown_guest = Select(driver.find_element(By.ID, "number-guests"))
    options = dropdown_guest.options
    random_guest = random.choice(options[1:])  # Skip the first option which is usually a placeholder
    dropdown_guest.select_by_visible_text(random_guest.text)
    time.sleep(1)
    driver.find_element(By.ID, "date").send_keys("24/03/2025")
    # Random time
    dropdown_time = Select(driver.find_element(By.ID, "time"))
    options = dropdown_time.options
    random_time = random.choice(options[1:])  # Skip the first option which is usually a placeholder
    dropdown_time.select_by_visible_text(random_time.text)
    time.sleep(1)
    driver.find_element(By.ID, "message").send_keys("Random message")
    time.sleep(2)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/#reservation", "Form was submitted despite invalid values"

def test_invalid_phone(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[7]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys("Shura")
    driver.find_element(By.ID, "email").send_keys("shura@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("abc123456")
    time.sleep(1)
    # Random guest
    dropdown_guest = Select(driver.find_element(By.ID, "number-guests"))
    options = dropdown_guest.options
    random_guest = random.choice(options[1:])  # Skip the first option which is usually a placeholder
    dropdown_guest.select_by_visible_text(random_guest.text)
    time.sleep(1)
    driver.find_element(By.ID, "date").send_keys("24/03/2025")
    # Random time
    dropdown_time = Select(driver.find_element(By.ID, "time"))
    options = dropdown_time.options
    random_time = random.choice(options[1:])  # Skip the first option which is usually a placeholder
    dropdown_time.select_by_visible_text(random_time.text)
    time.sleep(1)
    driver.find_element(By.ID, "message").send_keys("Random message")
    time.sleep(2)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/#reservation", "Form was submitted despite invalid values"

def test_required_fields_left_blank(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[7]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "form-submit").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/", "Form was submitted despite invalid values"

