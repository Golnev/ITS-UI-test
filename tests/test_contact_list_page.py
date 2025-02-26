import logging as logger

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.host_config import base_url
from src.pages.add_new_contact_page import AddNewContactPage
from src.pages.contact_details_page import ContactDetailsPage
from src.pages.contact_list_page import ContactListPage


@pytest.mark.contact_list
class TestContactListPage:
    logger.info("Starting tests for contact list page.")

    def test_user_should_be_in_contact_list_page(
        self, browser: webdriver.Firefox | webdriver.Chrome, setup_user
    ):
        logger.info("Starting Test: user should be in contact list page.")

        link = base_url + "contactList"
        page = ContactListPage(browser=browser, url=link)
        page.open()
        page.should_be_contact_list_page()

    def test_logout(self, browser: webdriver.Firefox | webdriver.Chrome, setup_user):
        logger.info("Starting Test: logout.")

        link = base_url + "contactList"
        page = ContactListPage(browser=browser, url=link)
        page.open()
        page.logout()

        WebDriverWait(browser, 10).until(EC.url_to_be(base_url))

        assert (
            page.browser.current_url == base_url
        ), f"Wrong URL after logout. URL: {page.browser.current_url}"

    def test_user_can_go_to_add_new_contact(
        self, browser: webdriver.Firefox | webdriver.Chrome, setup_user
    ):
        logger.info("Starting Test: user can go to add new contact.")

        link = base_url + "contactList"
        page = ContactListPage(browser=browser, url=link)
        page.open()
        page.go_to_add_new_contact()

        add_new_contact_page = AddNewContactPage(
            browser=browser, url=browser.current_url
        )
        add_new_contact_page.should_be_add_new_contact_page()

    def test_user_can_go_to_contact_details(
        self,
        browser: webdriver.Firefox | webdriver.Chrome,
        setup_user,
        create_contact_info,
    ):
        logger.info("Starting Test: user can go to contact details.")
        add_new_contact_link = base_url + "addContact"
        page = AddNewContactPage(browser=browser, url=add_new_contact_link)
        page.open()

        page.add_new_contact(*create_contact_info)

        WebDriverWait(browser, 10).until(EC.url_to_be(base_url + "contactList"))

        contact_list_page = ContactListPage(browser=browser, url=browser.current_url)

        contact_list_page.go_to_contact_details_by_full_name(
            first_name=create_contact_info[0], last_name=create_contact_info[1]
        )

        contact_details_page = ContactDetailsPage(
            browser=browser, url=browser.current_url
        )
        contact_details_page.should_be_contact_details_page()
