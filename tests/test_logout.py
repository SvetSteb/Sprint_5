from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class TestLogout:
# 3.1 Проверка отсутствия имени пользователя на странице после выхода из УЗ 
    def test_logout_check_no_username(self, login_user):
        driver = login_user
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON)))
        try:
            driver.find_element(*Locators.USER_NAME)
            assert False, "Имя пользователя все еще на странице"
        except NoSuchElementException:
            assert True

# Проверка наличия кнопки "Вход и регистраиця" после выхода из УЗ
    def test_logout_check_login_button_is_displayed(self, login_user):
        driver = login_user
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON)))
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()
