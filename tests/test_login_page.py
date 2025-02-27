import logging as logger
import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.host_config import base_url
from src.pages.login_page import LoginPage
from src.pages.register_page import RegisterPage


load_dotenv()


@pytest.mark.login
class TestLoginPage:
    logger.info("Starting tests for Login Page")

    def test_user_should_be_in_login_page(
        self, browser: webdriver.Firefox | webdriver.Chrome
    ):
        logger.info("Starting Test: user should be in login page")
        link = base_url + "login"
        page = LoginPage(browser=browser, url=link)
        page.open()
        page.should_be_login_page()

    def test_login(self, browser: webdriver.Firefox | webdriver.Chrome, setup_user):
        logger.info("Starting Test: login")
        link = base_url + "login"
        page = LoginPage(browser=browser, url=link)
        page.open()

        email = os.getenv("MY_EMAIL")
        password = os.getenv("MY_PASSWORD")

        if email and password:
            page.login(email=email, password=password)

        WebDriverWait(browser, 10).until(EC.url_to_be(base_url + "contactList"))

        assert (
            page.browser.current_url == base_url + "contactList"
        ), f"Wrong URL after login. URL: {page.browser.current_url}"

    def test_user_can_go_to_register_page(
        self, browser: webdriver.Firefox | webdriver.Chrome
    ):
        logger.info("Starting Test: go to register page.")
        link = base_url + "login"
        page = LoginPage(browser=browser, url=link)
        page.open()

        page.go_to_register_page()

        register_page = RegisterPage(browser=browser, url=browser.current_url)
        register_page.should_be_register_page()
