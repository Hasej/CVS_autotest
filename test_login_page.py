from .Pages.login_page import LoginPage

def test_login_page_appear(browser):
    link = "https://stagingv2-cvs.instantcard.net/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_email_field()
    page.should_be_email_field_label()
    page.should_be_password_field()
    page.should_be_password_field_label()
    page.should_be_remember_me_checkbox()
