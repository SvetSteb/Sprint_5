# Sprint 5
## tests/
#### 1. Тесты регистрации в файле test_registration.py
* 1.1 Проверка имени пользователя после успешной ргистрации - **test_correct_registration_check_user_name_is_User**
* 1.2 Проверка перехода на главную страницу после успешной регистрации - **test_correct_registration_check_is_home_page**
* 1.3 Проверка иконки для авара пользователя после успешной регистрации - **test_correct_registration_avatar_is_displayed**
* 1.4 Проверка изменения цвета границ полей после неуспешной регистрации **test_incorrect_email_borders_colour_is_red**
* 1.5 Проверка сообщения об ошибке после неуспешной регистрации **test_incorrect_email_error_message_appear**
* 1.6 Проверка изменения цвета границ и сообщения об ошибке при повторной регистрации с существующим email **test_registration_existing_user_borders_colour_is_red_and_error_message**

#### 2. Тест входа test_login.py
* 2.1 Проверка отображения имени пользователя после входа с зарегистрированной УЗ -  **test_login_user_name_is_User**
* 2.2 Проверка главной страницы после логина **test_login_check_page_is_home_page_with_search**
* 2.3 Проверка аватара после логина **test_login_check_avatar_is_displayed**

#### 3. Тест выхода из УЗ test_logout.py
* 3.1 Проверка отсутствия имени пользователя на странице после выхода из УЗ - **test_logout_check_no_username**
* 3.2 Проверка наличия кнопки "Вход и регистраиця" после выхода из УЗ - **test_logout_check_login_button_is_displayed**

#### 4. Тест размещения объявления 
* 4.1 Разместить объявление неавторизованным пользователем **test_add_advertisement_with_no_auth_check_error_message**
* 4.2 Раместить объявление авторизованным пользователем **test_add_adv_by_auth_user_check_new_adv** **test_get_book_genre_for_book_in_dict_without_genre_return_empty_line**

## Описание файлов проекта
locators.py - Содержит все используемые локаторы
helpers.py - содержит вспомогательные методы
data.py - содержит вспомогательные переменные для тестов
conftest.py - содержит требуемые фикстуры
