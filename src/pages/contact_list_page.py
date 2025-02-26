import logging as logger

from selenium.webdriver.common.by import By

from src.locators import ContactListPageLocators
from src.pages.base_page import BasePage


class ContactListPage(BasePage):
    def should_be_contact_list_page(self):
        self.should_be_contact_list_url()
        self.should_be_add_new_contact_button()
        self.should_be_contact_list_table()

    def should_be_contact_list_url(self):
        logger.info("Check contact list url.")

        assert (
            self.browser.current_url == ContactListPageLocators.CONTACT_LIST_PAGE_URL
        ), "URL address is not correct."

    def should_be_add_new_contact_button(self):
        logger.info("Check add new contact button is present.")

        assert self.is_element_present(
            *ContactListPageLocators.ADD_NEW_CONTACT_BUTTON
        ), "Add new contact button is not present."

    def should_be_contact_list_table(self):
        logger.info("Check contact list table is present.")

        assert self.is_element_present(
            *ContactListPageLocators.CONTACT_LIST_TABLE
        ), "Contact list table is not present."

    def logout(self):
        logger.info("Logout.")

        logout_button = self.browser.find_element(
            *ContactListPageLocators.LOGOUT_BUTTON
        )
        logout_button.click()

    def go_to_add_new_contact(self):
        logger.info("Go to add new contact page.")

        add_new_contact_button = self.browser.find_element(
            *ContactListPageLocators.ADD_NEW_CONTACT_BUTTON
        )
        add_new_contact_button.click()

    def find_contact_by_full_name(self, first_name: str, last_name: str):
        logger.info("Find contact by full name.")

        full_name = " ".join([first_name, last_name])
        rows = self.browser.find_elements(*ContactListPageLocators.FULL_NAME_CONTACTS)

        list_of_all_full_names = [row.text for row in rows]

        assert (
            full_name in list_of_all_full_names
        ), f"{first_name} {last_name} not in the contact list."

    def contact_is_not_present_in_contact_list(self, first_name: str, last_name: str):
        full_name = " ".join([first_name, last_name])

        rows = self.browser.find_elements(*ContactListPageLocators.FULL_NAME_CONTACTS)

        list_of_all_full_names = [row.text for row in rows]

        assert (
            full_name not in list_of_all_full_names
        ), f"{first_name} {last_name} in the contact list."

    def go_to_contact_details_by_full_name(self, first_name: str, last_name: str):
        logger.info("Go to contact details by full name.")

        full_name = " ".join([first_name, last_name])
        contact = self.browser.find_element(
            By.XPATH, f"//table//td[contains(text(), '{full_name}')]"
        )
        contact.click()

    def get_first_contact(self):
        logger.info("Get first contact from list.")

        if self.is_element_present(*ContactListPageLocators.FIRST_CONTACT):
            first_contact = self.browser.find_element(
                *ContactListPageLocators.FIRST_CONTACT
            )
            return first_contact

        logger.info("No contacts.")
        return
