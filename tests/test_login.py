from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import User


class TestLogin:
# 2.1 Проверка отображения имени пользователя после входа с зарегистрированной УЗ
    def test_login_user_name_is_User(self, driver):

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON)))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(User.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_USER_BUTTON)))
        driver.find_element(*Locators.LOGIN_USER_BUTTON).click()
        # Ожидаение появления имени пользователя
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.USER_NAME))
        user_name = driver.find_element(*Locators.USER_NAME).text 
        assert user_name == "User."

    #для практики последующие тесты используют фикстуру login_user
# 2.2 Проверка главной страницы после логина test_login_check_page_is_home_page_with_search
    def test_login_check_page_is_home_page_with_search(self, login_user):
        driver = login_user
        # Ожидаение появления строки поиска
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SEARCH_FIELD))
        search_field = driver.find_element(*Locators.SEARCH_FIELD).get_attribute('placeholder')
        assert search_field == "Я хочу купить..."

        # 2.3 Проверка аватара после логина test_login_check_avatar_is_displayed
    def test_login_check_avatar_is_displayed(self, login_user):
        driver = login_user
        # Ожидаение появления иконки пользователя
        WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((Locators.AVATAR),))
        assert driver.find_element(*Locators.AVATAR).is_displayed()

