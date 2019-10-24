from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket");
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1");
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color");
    BASKET  = (By.CSS_SELECTOR, "div.basket-mini");
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success");

    def GetAddedToCartSelector(product_name):
        return (By.XPATH, f"//strong[text()=\"{product_name}\"]");


