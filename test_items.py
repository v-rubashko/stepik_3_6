import time
from selenium.webdriver.common.by import By

def test_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    add_button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert len(add_button) > 0, 'Button "Add to basket" is not found'