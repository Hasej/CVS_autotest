from .base_page import BasePage
from .locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):

    def should_be_correct_reset_password_page(self):
        self.should_be_reset_password_url()
        self.should_be_email_field_on_reset_password()
        self.should_be_email_field_label_on_reset_password()
        self.should_be_sign_in_button_on_reset_password()
        self.should_be_reset_password_button_on_reset_password()



    def should_be_reset_password_url(self):
            assert "password/new" in self.browser.current_url, "Reset password url is not correct"

    def should_be_email_field_on_reset_password(self):
        assert self.is_element_present(*ResetPasswordLocators.RESET_EMAIL_FIELD), "Email field missed on Reset password page"

    def should_be_email_field_label_on_reset_password(self):
        assert self.is_element_present(*ResetPasswordLocators.RESET_EMAIL_FIELD_LABEL), "Email field label missed on Reset password page"

    def should_be_reset_password_button_on_reset_password(self):
        assert self.is_element_present(*ResetPasswordLocators.RESET_PASSWORD_BUTTON), "Reset password button missed on Reset password page"

    def should_be_sign_in_button_on_reset_password(self):
        assert self.is_element_present(*ResetPasswordLocators.SIGN_IN_BUTTON), "Sign in button missed on reset password page"


