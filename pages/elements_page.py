import time
import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS_FIELD).send_keys(permanent_address)
        self.scroll_down()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def expand_all_checkboxes(self):
        self.element_is_visible(self.locators.EXPEND_ALL_BUTTON).click()

    def check_random_checkboxes(self):
        checkbox_list = self.elements_are_visible(self.locators.CHECKBOX_LIST)
        count = 11
        while count != 0:
            item = checkbox_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_checkbox_list = self.elements_are_present(self.locators.CHECKED_CHECKBOXES)
        data = []
        for i in checked_checkbox_list:
            title_item = i.find_element("xpath", self.locators.TITLE_CHECKBOX)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_results(self):
        output_results = self.elements_are_present(self.locators.OUTPUT_RESULTS)
        output_data = []
        for i in output_results:
            output_data.append(i.text)
        return str(output_data).replace(' ', '').lower()
