from selenium.webdriver.common.by import By

class LoginPageLocators():
    EMAIL_FIELD = (By.ID, "user_email")
    EMAIL_FIELD_LABEL = (By.CSS_SELECTOR, ".email.input .label")
    PASSWORD_FIELD = (By.ID, "user_password")
    PASSWORD_FIELD_LABEL = (By.CSS_SELECTOR, ".password.input .label")
    REMEMBER_ME_CHECKBOX = (By.ID, "user_remember_me")
    NOT_REGISTERED_BLOCK = (By.CSS_SELECTOR, "p>a")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "#login>a")
    LOGIN_BUTTON = (By.ID, "user_submit_action")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "flash_notice")

class ResetPasswordLocators():
    RESET_EMAIL_FIELD = (By.ID, "user_email")
    RESET_EMAIL_FIELD_LABEL = (By.CSS_SELECTOR, ".email.input .label")
    RESET_PASSWORD_BUTTON = (By.ID, "user_submit_action")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#login>a")
    VALIDATION_ERROR_MESSAGE = (By.ID, "error_explanation")
    INLINE_ERRORS = (By.CLASS_NAME, "inline-errors")