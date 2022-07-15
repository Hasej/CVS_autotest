from .base_page import BasePage
from .locators import BasePageLocators

class EmployeePage(BasePage):
    def should_be_action_button_1(self):
        assert self.is_element_present(*BasePageLocators.ACTION_BUTTON2), "Action button missed"
        action_button_1 = self.browser.find_element(*BasePageLocators.ACTION_BUTTON2)
        action_button1_text = action_button_1.text
        assert "All Accounts" == action_button1_text, "Incorrect text"