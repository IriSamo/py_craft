import time

from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            time.sleep(1)
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()

            assert full_name == output_full_name
            assert email == output_email
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.expand_all_checkboxes()
            check_box_page.check_random_checkboxes()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_results = check_box_page.get_output_results()
            print()
            print(input_checkboxes)
            print(output_results)
            assert input_checkboxes == output_results


    class TestRadioButton:

        def test_radio_button_yes(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_yes_radio_button()
            text = radio_button_page.get_selected_radio_button()
            print()
            print(text)
            assert text == 'Yes'

        def test_button_yes(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_yes_button()
            text = radio_button_page.get_selected_radio_button()
            print()
            print(text)
            assert text == 'Yes'

        def test_radio_button_impressive(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_impressive_radio_button()
            text = radio_button_page.get_selected_radio_button()
            print()
            print(text)
            assert text == 'Impressive'

        def test_radio_button_choice(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            yes_selected = radio_button_page.get_selected_radio_button()
            print(yes_selected)
            radio_button_page.click_on_the_radio_button('impressive')
            impressive_selected = radio_button_page.get_selected_radio_button()
            print(impressive_selected)
            radio_button_page.click_on_the_radio_button('no')
            no_selected = radio_button_page.get_selected_radio_button()
            print(no_selected)

            assert yes_selected == 'Yes'
            assert impressive_selected == 'Impressive'
            # assert no_selected == None