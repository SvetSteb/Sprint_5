import pytest
from selenium import webdriver
from data import Urls, User
import random
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def user_email():    
    email = f'svetlana{random.randint(0,999)}@test.net'
    return email

@pytest.fixture
def exist_user(driver, user_email):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGOUT_BUTTON)))
             
        return [user_email, driver]

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON)))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(User.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_USER_BUTTON)))
        driver.find_element(*Locators.LOGIN_USER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGOUT_BUTTON)))   
        return driver
