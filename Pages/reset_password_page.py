from .base_page import BasePage
from .locators import ResetPasswordLocators
from .locators import LoginPageLocators

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


    def should_be_error_message_when_email_empty(self):
        button1= self.browser.find_element(*ResetPasswordLocators.RESET_PASSWORD_BUTTON)
        button1.click()

        assert self.is_element_present(*ResetPasswordLocators.VALIDATION_ERROR_MESSAGE), "Validation errors block not appear"

        error_message1 = self.browser.find_element(*ResetPasswordLocators.INLINE_ERRORS)
        error_text1 = error_message1.text
        assert error_text1 == "can't be blank", "Incorrect error message when email field empty"

    def should_be_error_message_when_email_incorrect(self):
        email_input=self.browser.find_element(*ResetPasswordLocators.RESET_EMAIL_FIELD)
        email_input.send_keys("test")

        button2= self.browser.find_element(*ResetPasswordLocators.RESET_PASSWORD_BUTTON)
        button2.click()

        assert self.is_element_present(*ResetPasswordLocators.VALIDATION_ERROR_MESSAGE), "Validation errors block not appear"

        error_message2 = self.browser.find_element(*ResetPasswordLocators.INLINE_ERRORS)
        error_text2 = error_message2.text
        assert error_text2 == "not found", "Incorrect error message when email incorrect"

    def should_be_success_reset_password(self):
        email_input = self.browser.find_element(*ResetPasswordLocators.RESET_EMAIL_FIELD)
        email_input.send_keys("shevtsov.t@gmail.com")

        button2 = self.browser.find_element(*ResetPasswordLocators.RESET_PASSWORD_BUTTON)
        button2.click()


    def should_be_correct_success_page(self):
        assert "login" in self.browser.current_url, "Navigated to incorrect link after restore password"

        success_message = self.browser.find_element(*LoginPageLocators.SUCCESS_MESSAGE)
        success_text = success_message.text
        assert "You will receive an email with instructions about how to reset your password in a few minutes." == success_text, "Success message text incorrect"
