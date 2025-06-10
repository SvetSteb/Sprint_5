from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']") # Кнопка Вход и регистрация
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']") # Кнопка Нет аккаунта
    EMAIL_FIELD = (By.XPATH, ".//input[(@class='input_inputStandart__JweLZ spanGlobal') and (@name='email')]") #Поле email
    PASSWORD_FIELD = (By.XPATH, ".//input[(@class='input_inputStandart__JweLZ spanGlobal') and (@name='password')]") # Поле Пароль
    PASSWORD_SUBMIT_FIELD = (By.XPATH, ".//input[(@class='input_inputStandart__JweLZ spanGlobal') and (@name='submitPassword')]") # Поле Подтверждение пароля
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']") # Кнопка Создать аккаунт
    AVATAR = (By.XPATH, ".//button[@class='circleSmall']") # Иконка профиля пользователя
    USER_NAME = (By.XPATH, ".//div[@class='columnSmall']/h3[@class='profileText name']") # Имя авторизованного пользователя
    ERROR_BORDERS_FIELD = (By.CLASS_NAME, "input_inputError__fLUP9") # Поля регистрационных данных при некорректном вводе данных
    ERROR_MESSAGE_REG = (By.XPATH, ".//span[text()='Ошибка']")
    LOGOUT_BUTTON = (By.XPATH, ".//div[@class='columnSmall']/button[@class='spanGlobal btnSmall']") # Кнопка Выйти
    LOGIN_USER_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка Войти
    SEARCH_FIELD = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal']") # строка поиска на главной
    ADD_ADV_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    AUTH_FORM = (By.CLASS_NAME, "popUp_shell__LuyqR") #Всплывающая форма авторизации
    AUTH_REQUIREMENT_MESSAGE = (By.XPATH, ".//div[@class='popUp_titleRow__M7tGg']/h1") #заголовок формы с требованием авторизации
    ADV_NAME_FIELD = (By.XPATH, ".//div[@class='input_inputDefault__UmPK0']/input[@name='name']") # Поле Название формы создания объявления
    CATEGORY_DROP_MENU = (By.XPATH, ".//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']") # Меню Категории
    CATEGORY_BOOKS = (By.XPATH, ".//span[(@class='undefined dropDownMenu_textColor__Nyo8k') and (text()='Книги')]") # Пункт меню Книги
    CONDITION_BY = (By.XPATH, ".//div[@class='radioUnput_shell__Wtdwe']/div[@class='radioUnput_inputRegular__FbVbr']") # Переключатель, состояние: БУ
    CITY_DROP_MENU = (By.XPATH, ".//form/div[@class='dropDownMenu_dropMenu__sBxhz']/div[@class='dropDownMenu_input__itKtw']/button") # Меню города
    CITY_N = (By.XPATH, ".//span[(@class='undefined dropDownMenu_textColor__Nyo8k') and (text()='Новосибирск')]") # Пункт меню Новосибирск
    DESCRIPTION_FIELD = (By.XPATH, ".//textarea[@name='description']") #Поле Описание
    PRICE_FIELD = (By.XPATH, ".//input[@name='price']") # Поле Цена
    SUBMIT_ADV_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']") # Кнопка Опубликовать для объявления
    LAST_USER_ADV = (By.XPATH, ".//div[@class='profilePage_listningBlock__Fi6E5']/*/*/div[@class='card']") # созданное объявление пользователя
    NAME_LAST_CARD = (By.XPATH, ".//div[@class='description']/div[@class='about']/h2") # Название последнего объявления пользователя