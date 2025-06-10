from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


class TestAddAdvertisement:

    # 4.1 Разместить объявление неавторизованным пользователем test_add_advertisement_with_no_auth_check_error_message
    def test_add_advertisement_with_no_auth_check_error_message(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ADD_ADV_BUTTON)))
        driver.find_element(*Locators.ADD_ADV_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.AUTH_FORM))) 
        title = driver.find_element(*Locators.AUTH_REQUIREMENT_MESSAGE).text
        assert title == 'Чтобы разместить объявление, авторизуйтесь'


    # 4.2 Разместить объявление от авторизованного пользователя 
    def test_add_adv_by_auth_user_check_new_adv(self, exist_user):
        # для теста создается новый пользователь из-за ограничения в 3 объявления от одного пользователя
        driver = exist_user[1]
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ADD_ADV_BUTTON)))
        driver.find_element(*Locators.ADD_ADV_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ADV_NAME_FIELD)))

        #Добавить название, сгенерированное случайно
        adv_name = helpers.random_adv_name()
        driver.find_element(*Locators.ADV_NAME_FIELD).send_keys(adv_name)

        #Выбрать категорию
        driver.find_element(*Locators.CATEGORY_DROP_MENU).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.CATEGORY_BOOKS)))
        driver.find_element(*Locators.CATEGORY_BOOKS).click()

        #указать состояние товара как Б.У
        driver.find_element(*Locators.CONDITION_BY).click()
        #указать город
        driver.find_element(*Locators.CITY_DROP_MENU).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.CITY_N)))
        driver.find_element(*Locators.CITY_N).click()
        # Добавить описание товара
        driver.find_element(*Locators.DESCRIPTION_FIELD).send_keys('Замечательный товар, тестовая карточка')
        #Цена
        driver.find_element(*Locators.PRICE_FIELD).send_keys(2500)
        driver.find_element(*Locators.SUBMIT_ADV_BUTTON).click()
        
        # Из-за частой ошибки stale element reference при медленной загрузке страницы при
        # переходе между страницами, использован вспомогательный метод с try-except

        helpers.safe_click(driver, *Locators.AVATAR)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((Locators.LAST_USER_ADV)))
        card = driver.find_element(*Locators.LAST_USER_ADV)
        driver.execute_script("arguments[0].scrollIntoView();", card) 
        published_adv_name = driver.find_element(*Locators.NAME_LAST_CARD).text
        assert published_adv_name == adv_name


