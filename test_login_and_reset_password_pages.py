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
    reset_page.should_naviagate_to_login_page_when_click_signin()


def test_reset_page_validation_errors(browser):
    link = "https://stagingv2-cvs.instantcard.net/password/new"
    page = ResetPasswordPage(browser, link)
    page.open()
    page.should_be_error_message_when_email_empty()
    page.should_be_error_message_when_email_incorrect()

def test_reset_password_success(browser):
    link = "https://stagingv2-cvs.instantcard.net/password/new"
    page = ResetPasswordPage(browser, link)
    page.open()
    page.should_be_success_reset_password()
    success_link = ResetPasswordPage(browser, browser.current_url)
    success_link.should_be_correct_success_page()

def test_login_page_validation_errors(browser):
    link = "https://stagingv2-cvs.instantcard.net/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_error_when_email_and_pass_empty()
    page.should_be_error_when_pass_empty()
    page.should_be_error_when_pass_incorrect()
    page.should_be_logged_in_with_correct_credentials()

