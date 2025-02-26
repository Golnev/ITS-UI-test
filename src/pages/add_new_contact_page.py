import logging as logger

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.locators import AddNewContactPageLocators
from src.pages.base_page import BasePage


class AddNewContactPage(BasePage):
    def should_be_add_new_contact_page(self):
        self.should_be_contact_list_url()
        self.should_be_add_new_contact_form()

    def should_be_contact_list_url(self):
        logger.info("Check contact list url.")

        assert (
            self.browser.current_url
            == AddNewContactPageLocators.ADD_NEW_CONTACT_PAGE_URL
        ), "URL address is not correct."

    def should_be_add_new_contact_form(self):
        logger.info("Check add new contact form is present.")

        assert self.is_element_present(
            *AddNewContactPageLocators.ADD_NEW_CONTACT_FORM
        ), "Add new contact form is not present."

    def logout(self):
        logger.info("Logout.")

        logout_button = self.browser.find_element(
            *AddNewContactPageLocators.LOGOUT_BUTTON
        )
        logout_button.click()

    def cancel_from_add_new_contact_page(self):
        logger.info("Cancel from add new contact page")

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(AddNewContactPageLocators.CANCEL_BUTTON)
        )

        cancel_button = self.browser.find_element(
            *AddNewContactPageLocators.CANCEL_BUTTON
        )

        cancel_button.click()

    def add_new_contact(
        self,
        first_name,
        last_name,
        date_of_birth,
        email,
        phone,
        street_address_1,
        city,
        state,
        postal_code,
        country,
    ):
        logger.info(
            f"Add new contact, with first name: {first_name}, last name: {last_name}"
        )

        first_name_form = self.browser.find_element(
            *AddNewContactPageLocators.FIRST_NAME
        )
        first_name_form.send_keys(first_name)

        last_name_form = self.browser.find_element(*AddNewContactPageLocators.LAST_NAME)
        last_name_form.send_keys(last_name)

        date_of_birth_form = self.browser.find_element(
            *AddNewContactPageLocators.DATE_OF_BIRTH
        )
        date_of_birth_form.send_keys(date_of_birth)

        email_form = self.browser.find_element(*AddNewContactPageLocators.EMAIL)
        email_form.send_keys(email)

        phone_form = self.browser.find_element(*AddNewContactPageLocators.PHONE)
        phone_form.send_keys(str(phone))

        street_address_1_form = self.browser.find_element(
            *AddNewContactPageLocators.STREET_ADDRESS_1
        )
        street_address_1_form.send_keys(street_address_1)

        city_form = self.browser.find_element(*AddNewContactPageLocators.CITY)
        city_form.send_keys(city)

        state_form = self.browser.find_element(*AddNewContactPageLocators.STATE)
        state_form.send_keys(state)

        postal_code_form = self.browser.find_element(
            *AddNewContactPageLocators.POSTAL_CODE
        )
        postal_code_form.send_keys(str(postal_code))

        country_form = self.browser.find_element(*AddNewContactPageLocators.COUNTRY)
        country_form.send_keys(country)

        submit_button = self.browser.find_element(
            *AddNewContactPageLocators.SUBMIT_BUTTON
        )
        submit_button.click()
