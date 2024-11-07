# http://127.0.0.1:8000
# pytest Test_Cart_Checkout.py

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

def test_add_item_to_cart(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div[2]/div/div/div[2]/a/input").click()
    time.sleep(2)
    # Random quantity
    random_number = random.randint(1, 10)
    number_input = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/input[2]")
    number_input.clear()  # Xóa giá trị hiện tại
    number_input.send_keys(str(random_number))
    driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/button").click()
    time.sleep(2)
    cart_count =  driver.find_element(By.ID, "lblCartCount").text
    assert "1" in cart_count

def test_place_order(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div[2]/div/div/div[2]/a/input").click()
    time.sleep(2)
    # Random quantity
    random_number = random.randint(1, 10)
    number_input = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/input[2]")
    number_input.clear()  # Xóa giá trị hiện tại
    number_input.send_keys(str(random_number))
    driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[8]/a/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/table/tfoot/tr[5]/td/form/button").click()
    time.sleep(2)
    driver.find_element(By.ID, "cod").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/input[2]").click()
    time.sleep(2)
    driver.find_element(By.ID, "address").clear()
    driver.find_element(By.ID, "address").send_keys("123 abc")
    # Tìm dropdown bằng ID
    country_select = Select(driver.find_element(By.ID, "country"))
    # Chọn giá trị "Bangladesh"
    country_select.select_by_visible_text("Bangladesh")
    # State
    state_select = Select(driver.find_element(By.ID, "state"))
    
    state_select.select_by_visible_text("Dhaka")
    driver.find_element(By.ID, "zip").send_keys("123456")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button").click()
    time.sleep(2)
    message = driver.find_element(By.XPATH, "/html/body/div/h1").text
    assert "Success" in message

def test_cart_empty_after_order(driver):
    test_place_order(driver)
    driver.get("http://127.0.0.1:8000/cart")
    time.sleep(2)
    cart_count =  driver.find_element(By.ID, "lblCartCount").text
    assert "0" in cart_count, "Cart should be empty after checkout"

def test_pay_with_online(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div[2]/div/div/div[2]/a/input").click()
    time.sleep(2)
    # Random quantity
    random_number = random.randint(1, 10)
    number_input = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/input[2]")
    number_input.clear()  # Xóa giá trị hiện tại
    number_input.send_keys(str(random_number))
    driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[8]/a/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/table/tfoot/tr[5]/td/form/button").click()
    time.sleep(2)
    driver.find_element(By.ID, "bkash").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/a/input").click()
    time.sleep(2)
    driver.find_element(By.ID, "address").clear()
    driver.find_element(By.ID, "address").send_keys("123 abc")
    # Tìm dropdown bằng ID
    country_select = Select(driver.find_element(By.ID, "country"))
    # Chọn giá trị "Bangladesh"
    country_select.select_by_visible_text("Bangladesh")
    # State
    state_select = Select(driver.find_element(By.ID, "state"))
    
    state_select.select_by_visible_text("Dhaka")
    driver.find_element(By.ID, "zip").send_keys("123456")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button").click()
    time.sleep(2)
    message = driver.find_element(By.XPATH, "/html/body/div/h1").text
    assert "Success" in message

def test_invalid_payment_infomations(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div[2]/div/div/div[2]/a/input").click()
    time.sleep(2)
    # Random quantity
    random_number = random.randint(1, 10)
    number_input = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/input[2]")
    number_input.clear()  # Xóa giá trị hiện tại
    number_input.send_keys(str(random_number))
    driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/form/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[8]/a/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/table/tfoot/tr[5]/td/form/button").click()
    time.sleep(2)
    driver.find_element(By.ID, "cod").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/input[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/div/h1").text
    assert "Error! All fields must be filled" in error_message, "Form accecpted empty fields"