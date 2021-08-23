from selenium.webdriver.common.by import By
import pytest



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK="http://selenium1py.pythonanywhere.com"
    
class LoginPageLocators():
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    



class ProductPageLocators():
    PARAM_LINK_HANDBOOK=""
    LINK_HANDBOOK="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    BASKET_BUTTON=(By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT=(By.CSS_SELECTOR, "h1")
    PRICE=(By.CSS_SELECTOR, ".price_color")
    
    
class BasketPageLocators():    
    MSG_PRODUCT_ADDED=(By.CSS_SELECTOR, ".alertinner :nth-child(1)") 
    PRICE_MSG=(By.CSS_SELECTOR, ".alert-info strong")