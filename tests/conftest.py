import logging as logger
import os

import pytest
from dotenv import load_dotenv
from faker import Faker
from selenium import webdriver


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.host_config import base_url
from src.pages.add_new_contact_page import AddNewContactPage
from src.pages.contact_details_page import ContactDetailsPage
from src.pages.contact_list_page import ContactListPage
from src.pages.login_page import LoginPage

load_dotenv()

firefox_path = os.getenv("FIREFOX_PATH")
geckodriver_path = os.getenv("GECKODRIVER_PATH")

google_chrome_path = os.getenv("GOOGLE_CHROME_PATH")
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")


def pytest_addoption(parser):
    parser.addoption(
        "--rm",
        action="store_true",
        default=False,
        help="Delete a created contact after test",
    )
    parser.addoption(
        "--browser_name",
        action="store",
        default="firefox",
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("--browser_name")
    browser = None

    if browser_name == "firefox":
        logger.info("Prepare browser firefox.")

        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service

        options = Options()
        if firefox_path and geckodriver_path:
            options.binary_location = firefox_path

            service = Service(executable_path=geckodriver_path)
            browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == "chrome":
        logger.info("Prepare browser chrome.")

        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service

        options = Options()
        if google_chrome_path and chromedriver_path:
            options.binary_location = google_chrome_path

            service = Service(executable_path=chromedriver_path)
            browser = webdriver.Chrome(service=service, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    logger.info("Browser quit.")
    if browser:
        browser.quit()


@pytest.fixture(autouse=True)
def del_all_contacts(browser: webdriver.Firefox | webdriver.Chrome, pytestconfig):
    yield
    if pytestconfig.getoption("--rm"):
        logger.info("Delete all contacts.")
        link = base_url + "contactList"
        contact_list_page = ContactListPage(browser=browser, url=link)
        contact_list_page.open()

        while True:
            first_contact = contact_list_page.get_first_contact()

            if first_contact:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable(first_contact)
                )
                first_contact.click()
                contact_details_page = ContactDetailsPage(
                    browser=browser, url=browser.current_url
                )
                contact_details_page.delete_contact()
                WebDriverWait(browser, 5).until(EC.staleness_of(first_contact))
                contact_list_page.open()
            else:
                break


@pytest.fixture(scope="function")
def setup_user(browser: webdriver.Firefox | webdriver.Chrome):
    logger.info("Setup user with default parameters.")
    link = base_url + "login"
    page = LoginPage(browser=browser, url=link)
    page.open()

    email = os.getenv("MY_EMAIL")
    password = os.getenv("MY_PASSWORD")

    if email and password:
        page.login(email=email, password=password)


@pytest.fixture(scope="function")
def create_contact_info(browser: webdriver.Firefox | webdriver.Chrome, setup_user):
    logger.info("Create contact.")
    link = base_url + "addContact"
    page = AddNewContactPage(browser=browser, url=link)
    page.open()

    fake = Faker()
    fake_contact_first_name = fake.first_name()
    fake_contact_last_name = fake.last_name()
    fake_contact_date_of_birth = (
        fake.date_of_birth(minimum_age=6, maximum_age=110)
    ).strftime("%Y-%m-%d")
    fake_contact_email = fake.email()
    fake_contact_phone = fake.basic_phone_number()
    fake_contact_street_address_1 = fake.street_name()
    fake_contact_city = fake.city()
    fake_contact_state = fake.state()
    fake_contact_postal_code = fake.postalcode()
    fake_contact_country = fake.country()[:40]

    return (
        fake_contact_first_name,
        fake_contact_last_name,
        fake_contact_date_of_birth,
        fake_contact_email,
        fake_contact_phone,
        fake_contact_street_address_1,
        fake_contact_city,
        fake_contact_state,
        fake_contact_postal_code,
        fake_contact_country,
    )


@pytest.fixture(scope="function")
def created_contact(
    browser: webdriver.Firefox | webdriver.Chrome,
    setup_user,
    create_contact_info,
    pytestconfig,
):
    logger.info(
        f"Creating contact wit\n"
        f"contact first name: {create_contact_info[0]}, last name: {create_contact_info[1]}"
    )
    add_new_contact_link = base_url + "addContact"
    page = AddNewContactPage(browser=browser, url=add_new_contact_link)
    page.open()

    page.add_new_contact(*create_contact_info)

    WebDriverWait(browser, 10).until(EC.url_to_be(base_url + "contactList"))

    contact_list_page = ContactListPage(browser=browser, url=browser.current_url)

    contact_list_page.go_to_contact_details_by_full_name(
        first_name=create_contact_info[0], last_name=create_contact_info[1]
    )

    contact_details_page = ContactDetailsPage(browser=browser, url=browser.current_url)

    return contact_details_page, create_contact_info
