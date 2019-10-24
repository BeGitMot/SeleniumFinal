from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket");
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1");
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color");
    BASKET  = (By.CSS_SELECTOR, "div.basket-mini");

    def GetAddedToCartSelector(product_name):
        return (By.XPATH, f"//strong[text()=\"{product_name}\"]");
