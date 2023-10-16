from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    CURRENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id = "currentAddress"]')
    PERMANENT_ADDRESS_FIELD = (By.XPATH, '//textarea[@id = "permanentAddress"]')
    SUBMIT_BUTTON = (By.ID, 'submit')

    # created form
    CREATED_FULL_NAME = (By.ID, 'name')
    CREATED_EMAIL = (By.ID, 'email')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id = "currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id = "permanentAddress"]')
