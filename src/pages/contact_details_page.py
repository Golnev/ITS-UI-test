import logging as logger
import time
from typing import Literal

from src.locators import ContactDetailsPageLocators
from src.pages.base_page import BasePage


class ContactDetailsPage(BasePage):
    def should_be_contact_details_page(self):
        self.should_be_contact_details_page_url()
        self.should_be_contact_details_form()

    def should_be_contact_details_page_url(self):
        logger.info("Check contacts details page url.")

        assert (
            self.browser.current_url
            == ContactDetailsPageLocators.CONTACT_DETAILS_PAGE_URL
        ), "URL address is not correct."

    def should_be_contact_details_form(self):
        logger.info("Check contact details form is present.")

        assert self.is_element_present(
            *ContactDetailsPageLocators.CONTACT_DETAILS_FORM
        ), "Contact details form is not present."

    def logout(self):
        logger.info("Logout.")

        logout_button = self.browser.find_element(
            *ContactDetailsPageLocators.LOGOUT_BUTTON
        )
        logout_button.click()

    def return_to_contact_list(self):
        logger.info("Return to contact list.")

        return_button = self.browser.find_element(
            *ContactDetailsPageLocators.RETURN_BUTTON
        )
        return_button.click()

    def delete_contact(self):
        logger.info("Deleting contact.")

        delete_button = self.browser.find_element(
            *ContactDetailsPageLocators.DELETE_BUTTON
        )
        delete_button.click()

        alert = self.browser.switch_to.alert
        alert.accept()

    def go_to_edit_contact_page(self):
        logger.info("Go to edit contact page.")

        edit_contact_button = self.browser.find_element(
            *ContactDetailsPageLocators.EDIT_CONTACT_BUTTON
        )
        edit_contact_button.click()

    def get_info(
        self,
        what: Literal[
            "first_name",
            "last_name",
            "date_of_birth",
            "email",
            "phone",
            "street_address_1",
            "street_address_2",
            "city",
            "state",
            "postal_code",
            "country",
        ],
    ):
        logger.info("Get info from field.")

        locators_dict = {
            "first_name": ContactDetailsPageLocators.FIRST_NAME,
            "last_name": ContactDetailsPageLocators.LAST_NAME,
            "date_of_birth": ContactDetailsPageLocators.DATE_OF_BIRTH,
            "email": ContactDetailsPageLocators.EMAIL,
            "phone": ContactDetailsPageLocators.PHONE,
            "street_address_1": ContactDetailsPageLocators.STREET_ADDRESS_1,
            "street_address_2": ContactDetailsPageLocators.STREET_ADDRESS_2,
            "city": ContactDetailsPageLocators.CITY,
            "state": ContactDetailsPageLocators.STATE,
            "postal_code": ContactDetailsPageLocators.POSTAL_CODE,
            "country": ContactDetailsPageLocators.COUNTRY,
        }

        time.sleep(3)
        field_text = self.get_visible_element(*locators_dict[what])

        return field_text
