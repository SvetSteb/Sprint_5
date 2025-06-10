import random
import string
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def random_adv_name(length = 8):
    cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    digits = string.digits
    all_chars = cyrillic_lower + digits
    random_adv_name = ''.join(random.choice(all_chars) for _ in range(8))
    return random_adv_name

def safe_click(driver, by, value, max_retries=3):
    for _ in range(max_retries):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()

        except StaleElementReferenceException:
            continue
