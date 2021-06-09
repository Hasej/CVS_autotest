from .base_page import BasePage
from .locators import LoginPageLocators
from .reset_password_page import ResetPasswordPage


class LoginPage(BasePage):

    def should_be_correct_login_page(self):
        self.should_be_login_url()
        self.should_be_email_field()
        self.should_be_email_field_label()
        self.should_be_password_field()
        self.should_be_email_field_label()
        self.should_be_remember_me_checkbox()
        self.should_be_forgot_password_link()
        self.should_be_not_registered_block()
        self.should_be_login_button()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not correct"

    def should_be_email_field(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "Email field is not presented"

    def should_be_email_field_label(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD_LABEL), "Email field label is not presented"

    def should_be_password_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Password field is not presented"

    def should_be_password_field_label(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD_LABEL), "Password field label is not presented"

    def should_be_remember_me_checkbox(self):
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_CHECKBOX), "Remember me checkbox is not presented"

    def should_be_not_registered_block(self):
        assert self.is_element_present(*LoginPageLocators.NOT_REGISTERED_BLOCK), "Not registered yet block is not presented"

    def should_be_forgot_password_link(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), "Forgot password is not presented"

    def should_be_correct_forgot_password_link(self):
        forgot_password = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD)
        forgot_password.click()
        assert 'password/new' in self.browser.current_url, "Forgot password link incorrect"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def go_to_reset_page(self):
        link = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD)
        link.click()
        #return ResetPasswordPage(browser=self.browser, url=self.browser.current_url)

