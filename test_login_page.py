from .Pages.login_page import LoginPage
from .Pages.reset_password_page import ResetPasswordPage

def test_login_page_appear(browser):
    link = "https://stagingv2-cvs.instantcard.net/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_correct_login_page()

def test_reset_password_page_appear(browser):
    link = "https://stagingv2-cvs.instantcard.net/login"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_reset_page()
    reset_page = ResetPasswordPage(browser, browser.current_url)
    reset_page.should_be_correct_reset_password_page()



