from .Pages.employees_page import EmployeePage
from .Pages.login_page import LoginPage

def test_action_button(browser):
    link = "https://stagingv2-cvs.instantcard.net/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_logged_in_with_correct_credentials()
    e_page = EmployeePage(browser, browser.current_url)
    e_page.should_be_action_button_1()