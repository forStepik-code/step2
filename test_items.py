from selenium.webdriver.support import expected_conditions as EC
import time


def test_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket = browser \
        .find_element_by_xpath("//button[contains(@class, 'btn-add-to-basket')]")

    # time.sleep(30)
    assert EC.visibility_of(basket), "There is not basket button"
