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
    LOGIN_ERROR_MESSAGE = (By.CLASS_NAME, "flash_alert")

class ResetPasswordLocators():
    RESET_EMAIL_FIELD = (By.ID, "user_email")
    RESET_EMAIL_FIELD_LABEL = (By.CSS_SELECTOR, ".email.input .label")
    RESET_PASSWORD_BUTTON = (By.ID, "user_submit_action")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#login>a")
    VALIDATION_ERROR_MESSAGE = (By.ID, "error_explanation")
    INLINE_ERRORS = (By.CLASS_NAME, "inline-errors")

class BasePageLocators():
    HEADER_LOGO_IMAGE = (By.ID, "site_title_image")
    HEADER_COMPANY_BUTTON = (By.ID, "company_page")
    HEADER_EMPLOYEE_BUTTON = (By.ID, "users")
    HEADER_CREDENTIALS_BUTTON = (By.ID, "credentials")
    HEADER_CREDENTIAL_SECTIONS_BUTTON = (By.ID, "credential_sections")
    HEADER_QUALIFICATIONS_BUTTON = (By.ID, "qualifications")
    HEADER_DOCUMENTS_BUTTON = (By.ID, "documents")
    HEADER_INFO_TABLE_BUTTON = (By.ID, "info_tables")
    HEADER_EQUIPMENT_BUTTON = (By.ID, "equipment")
    HEADER_LOG_REPORTS_BUTTON = (By.ID, "log_reports")
    HEADER_LOGGING_ENTITIES = (By.ID, "logging_entities")
    HEADER_REPORTS_BUTTON = (By.ID, "reports")
    HEADER_SCHEDULED_REPORTS_BUTTON = (By.ID, "scheduled_reports")
    HEADER_CURRENT_USER_BUTTON = (By.ID, "current_user")
    HEADER_LOGOUT_BUTTON = (By.ID, "logout")
    PAGE_TITLE = (By.ID, "page_title")
    ACTION_BUTTON1 = (By.CLASS_NAME, ".action_item>a")
    ACTION_BUTTON2 = (By.CSS_SELECTOR, ".action_items:nth-child(2)>a")
    

