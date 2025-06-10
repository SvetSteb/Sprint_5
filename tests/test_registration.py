from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import User
import helpers


class TestRegistration:
# 1.1 Проверка имени пользователя после успешной ргистрации
    def test_correct_registration_check_user_name_is_User(self, driver):

        # Клик по кнопке Вход и регистрация
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Дождаться кнопки Нет аккаунта и кликнуть по ней
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()

        #сгенерировать новый email 
        user_email = helpers.user_email()

        # Дождаться поля формы регистрации и заполнить
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)

        # Нажать Создать аккаунт
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        # Ожидаение имени ползователя пользователя
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.USER_NAME)))
        user_name = driver.find_element(*Locators.USER_NAME).text 
        assert user_name == "User."

# 1.2 Проверка перехода на главную страницу после успешной регистрации
    def test_correct_registration_check_is_home_page(self, driver):
        # отличие в ОР, для независимости теста
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        user_email = helpers.user_email()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SEARCH_FIELD))
        search_field = driver.find_element(*Locators.SEARCH_FIELD).get_attribute('placeholder')
        assert search_field == "Я хочу купить..."

# 1.3 Проверка иконки для авара пользователя после успешной регистрации
    def test_correct_registration_avatar_is_displayed(self, driver):
        # отличие в ОР, для независимости теста
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        user_email = helpers.user_email()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.AVATAR)))
        assert driver.find_element(*Locators.AVATAR).is_displayed()

#  1.4 Проверка изменения цвета границ полей после неуспешной регистрации
    def test_incorrect_email_borders_colour_is_red(self, driver):

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        user_email = helpers.user_email()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email.replace('@', ''))
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ERROR_MESSAGE_REG)))
        #сохранить список из элементов - полей для ввода данных (почта, пароль, подтверждение пароля)
        fields_borders = driver.find_elements(*Locators.ERROR_BORDERS_FIELD)
        red_border = 0
        red = '1px solid rgb(255, 105, 114)' # красные границы, которые должны быть
        # все три элемента должны иметь красные границы
        for element in fields_borders:
            if element.value_of_css_property('border') == red:
                red_border += 1
        assert red_border == len(fields_borders)

# 1.5 Проверка сообщения об ошибке после неуспешной регистрации c email не по маске
    def test_incorrect_email_error_message_appear(self, driver):

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))
        user_email = helpers.user_email()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email.replace('@', ''))

        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ERROR_MESSAGE_REG)))
        assert driver.find_element(*Locators.ERROR_MESSAGE_REG).text == "Ошибка" 

# 1.6 Проверка изменения цвета границ и сообщения об ошибке при повторной регистрации с существующим email
    def test_registration_existing_user_borders_colour_is_red_and_error_message(self, driver):
        
        #Создать УЗ с ранее зарегистрированным email
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON)))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.NO_ACCOUNT_BUTTON)))
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EMAIL_FIELD)))

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(User.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.PASSWORD_SUBMIT_FIELD).send_keys(User.PASSWORD)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ERROR_MESSAGE_REG)))
        
        fields_borders = driver.find_elements(*Locators.ERROR_BORDERS_FIELD)
        red_border = 0
        red = '1px solid rgb(255, 105, 114)' # красные границы, которые должны быть
        # все три элемента должны иметь красные границы
        for element in fields_borders:
            if element.value_of_css_property('border') == red:
                red_border += 1
        assert red_border == len(fields_borders) and driver.find_element(*Locators.ERROR_MESSAGE_REG).text == "Ошибка"

