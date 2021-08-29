import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import BasketPage
from .pages.product_page import ProductPage


# @pytest.mark.parametrize('code', [0,1,2,3,4,5,6, pytest.param(7, marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    print(link)
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page_busket = BasketPage(browser, browser.current_url)

    page_busket.should_be_msg_same_produsct_added_to_basket()
    page_busket.should_be_single_price_with_product_added()
    # time.sleep(60)
    # page_busket.test_guest_cant_see_success_message_after_adding_product_to_basket()
    # page_busket.test_guest_cant_see_success_message
    # page_busket.test_message_disappeared_after_adding_product_to_basket()
    # page_busket.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PARAM_LINK_HANDBOOK)
    page.open()
    page.add_to_basket()

    page_busket = BasketPage(browser, browser.current_url)
    page_busket.should_not_be_success_message_by_is_not_element_present()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.PARAM_LINK_HANDBOOK)
    page.open()
    page=BasketPage(browser, browser.current_url)
    page.should_not_be_success_message_by_is_not_element_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PARAM_LINK_HANDBOOK)
    page.open()
    page.add_to_basket()
    page_busket = BasketPage(browser, browser.current_url)
    page_busket.should_not_be_success_message_by_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()