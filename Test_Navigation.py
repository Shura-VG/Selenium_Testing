# http://127.0.0.1:8000
# pytest Test_Navigation.py

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

def test_navigation_main_menu(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("jessica@gmail.com")
    driver.find_element(By.ID, "password").send_keys("69696969")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[4]/button").click()
    time.sleep(1)
    # Home
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[1]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    time.sleep(2)
    # About
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[2]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    time.sleep(2)
    # Menu
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[3]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    time.sleep(2)
    # Trace Order
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/trace-my-order"
    time.sleep(2)
    # My Order
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[5]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/my-order"
    time.sleep(2)
    # Chefs
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[6]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    time.sleep(2)
    # Contact Us
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[7]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    time.sleep(2)
    # Cart
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[8]/a").click()
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/cart"
    time.sleep(2)
    # Profile
    driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[10]/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/a").click()
    time.sleep(1)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/user/profile"
    time.sleep(1)

def test_navigation_icon(driver):
    driver.get("http://127.0.0.1:8000")
    time.sleep(2)
    # Icon header
    driver.find_element(By.XPATH,"/html/body/header/div/nav/a/img").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    # Icon footer
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/footer/div/div/div[2]/div/a/img").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "http://127.0.0.1:8000/"
    # Facebook
    driver.find_element(By.XPATH,"/html/body/footer/div/div/div[1]/div/ul/li[1]/a").click()
    current_url = driver.current_url
    assert current_url == "https://www.facebook.com/rahathosenmanik/?_rdc=1&_rdr"
    time.sleep(2)
    # Twitter
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/footer/div/div/div[1]/div/ul/li[2]/a").click()
    time.sleep(5)
    current_url = driver.current_url
    assert current_url == "https://x.com/i/flow/login?redirect_after_login=%2Frahathosenmanik"
    time.sleep(3)
    # Linkedin
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/footer/div/div/div[1]/div/ul/li[3]/a").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.linkedin.com/in/rahathossenmanik/"
    time.sleep(3)
    # Instagram
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/footer/div/div/div[1]/div/ul/li[4]/a").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.instagram.com/rahathossenmanik/?hl=en"
    time.sleep(2)
