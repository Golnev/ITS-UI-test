import logging as logger
import time
from typing import Literal

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from src.locators import EditContactPageLocators
from src.pages.base_page import BasePage


class EditContactPage(BasePage):
    def should_be_edit_contact_page(self):
        self.should_be_edit_contact_page_url()
        self.should_be_edit_contact_form()

    def should_be_edit_contact_page_url(self):
        logger.info("Check edit contact page url.")

        assert (
            self.browser.current_url == EditContactPageLocators.EDIT_CONTACT_PAGE_URL
        ), "URL address is not correct."

    def should_be_edit_contact_form(self):
        logger.info("Check edit contact form is present")

        assert self.is_element_present(
            *EditContactPageLocators.EDIT_CONTACT_FORM
        ), "Edit contact form is not present."

    def logout(self):
        logger.info("Logout from edit contact page.")

        logout_button = self.browser.find_element(
            *EditContactPageLocators.LOGOUT_BUTTON
        )
        logout_button.click()

    def return_to_contact_details(self):
        logger.info("Return to contact details from edit contact page.")

        cancel_button = self.browser.find_element(
            *EditContactPageLocators.CANCEL_BUTTON
        )
        cancel_button.click()

    def edit_contact(
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
        data: str,
    ):
        logger.info(f"Edit {what} contact with {data}.")

        locators_dict = {
            "first_name": EditContactPageLocators.FIRST_NAME,
            "last_name": EditContactPageLocators.LAST_NAME,
            "date_of_birth": EditContactPageLocators.DATE_OF_BIRTH,
            "email": EditContactPageLocators.EMAIL,
            "phone": EditContactPageLocators.PHONE,
            "street_address_1": EditContactPageLocators.STREET_ADDRESS_1,
            "street_address_2": EditContactPageLocators.STREET_ADDRESS_2,
            "city": EditContactPageLocators.CITY,
            "state": EditContactPageLocators.STATE,
            "postal_code": EditContactPageLocators.POSTAL_CODE,
            "country": EditContactPageLocators.COUNTRY,
        }

        edit_field = self.browser.find_element(*locators_dict[what])

        time.sleep(1)
        edit_field.send_keys(Keys.CONTROL + "a")
        edit_field.send_keys(Keys.DELETE)
        WebDriverWait(self.browser, 2).until(
            lambda driver: edit_field.get_attribute("value") == ""
        )

        edit_field.send_keys(data)

        submit_button = self.browser.find_element(
            *EditContactPageLocators.SUBMIT_BUTTON
        )
        submit_button.click()
