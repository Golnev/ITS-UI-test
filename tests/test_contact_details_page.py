import logging as logger

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.host_config import base_url
from src.pages.contact_details_page import ContactDetailsPage
from src.pages.contact_list_page import ContactListPage
from src.pages.edit_contact_page import EditContactPage


@pytest.mark.contact_details_page
class TestContactDetailsPage:
    logger.info("Starting tests for contact details page.")

    def test_user_should_be_in_contact_details_page(
        self,
        browser: webdriver.Firefox | webdriver.Chrome,
        setup_user,
        created_contact: tuple[ContactDetailsPage, tuple],
    ):
        logger.info("Starting Test: user should be in contact details page.")

        page, _ = created_contact

        page.should_be_contact_details_page()

    def test_logout_from_contact_details_page(
        self,
        browser: webdriver.Firefox | webdriver.Chrome,
        setup_user,
        created_contact: tuple[ContactDetailsPage, tuple],
    ):
        logger.info("Starting Test: logout from contact details page.")

        page, _ = created_contact

        page.logout()

        WebDriverWait(browser, 10).until(EC.url_to_be(base_url))

        assert (
            page.browser.current_url == base_url
        ), f"Wrong URL after logout. URL: {page.browser.current_url}"

    def test_return_to_contact_list(
        self,
        browser: webdriver.Firefox | webdriver.Chrome,
        setup_user,
        created_contact: tuple[ContactDetailsPage, tuple],
    ):
        logger.info("Starting Test: return to contact list.")

        page, _ = created_contact

        page.return_to_contact_list()

        contact_list_page = ContactListPage(browser=browser, url=browser.current_url)
        contact_list_page.should_be_contact_list_page()

    def test_delete_contact(
        self,
        browser: webdriver.Firefox | webdriver.Chrome,
        setup_user,
        created_contact: tuple[ContactDetailsPage, tuple],
    ):
        logger.info("Starting Test: delete contact.")

        page, contact_info = created_contact

        page.delete_contact()

        WebDriverWait(browser, 10).until(EC.url_to_be(base_url + "contactList"))

        contact_list_page = ContactListPage(browser=browser, url=browser.current_url)
        contact_list_page.should_be_contact_list_page()
        contact_list_page.contact_is_not_present_in_contact_list(
            first_name=contact_info[0], last_name=contact_info[1]
        )

    def test_user_can_go_to_edit_contact(
        self,
        browser: webdriver.Firefox | webdriver.Chrome,
        setup_user,
        created_contact: tuple[ContactDetailsPage, tuple],
    ):
        logger.info("Starting Test: user can go to edit contact.")

        page, _ = created_contact

        page.go_to_edit_contact_page()

        WebDriverWait(browser, 10).until(EC.url_to_be(base_url + "editContact"))

        edit_contact_page = EditContactPage(browser=browser, url=browser.current_url)
        edit_contact_page.should_be_edit_contact_page()
