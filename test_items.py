import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_exist(driver):
    driver.get(link)
    time.sleep(30)
    add_to_cart_btn = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    assert add_to_cart_btn, "Add to cart button is not present on the page"
