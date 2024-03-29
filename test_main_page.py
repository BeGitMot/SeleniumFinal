from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators, LoginPageLocators

MAIN_URL = "http://selenium1py.pythonanywhere.com/"
LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_URL)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_URL)
    page.open()
    page.should_be_login_link()
'''
def test_login_page(browser):
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.open()
    login_page.should_be_login_url()
    login_page.should_be_login_page()
    login_page.should_be_login_form()
'''


