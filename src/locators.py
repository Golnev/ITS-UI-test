from dataclasses import dataclass

from selenium.webdriver.common.by import By

from src.host_config import base_url


@dataclass
class LoginPageLocators:
    LOGIN_PAGE_URL: str = base_url + "login"
    LOGIN_FORM = (By.TAG_NAME, "form")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#signup")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")


@dataclass
class RegisterPageLocators:
    REGISTER_PAGE_URL: str = base_url + "addUser"
    REGISTER_FORM = (By.CSS_SELECTOR, "#add-user")
    REGISTER_FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    REGISTER_LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#submit")
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, "#error")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")


@dataclass
class ContactListPageLocators:
    CONTACT_LIST_PAGE_URL: str = base_url + "contactList"
    ADD_NEW_CONTACT_BUTTON = (By.CSS_SELECTOR, "#add-contact")
    CONTACT_LIST_TABLE = (By.CSS_SELECTOR, ".contactTable")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout")
    FULL_NAME_CONTACTS = (By.XPATH, "//table[@id='myTable']/tr/td[2]")


@dataclass
class AddNewContactPageLocators:
    ADD_NEW_CONTACT_PAGE_URL: str = base_url + "addContact"
    ADD_NEW_CONTACT_FORM = (By.CSS_SELECTOR, "#add-contact")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "#birthdate")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PHONE = (By.CSS_SELECTOR, "#phone")
    STREET_ADDRESS_1 = (By.CSS_SELECTOR, "#street1")
    CITY = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#stateProvince")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postalCode")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")


@dataclass
class ContactDetailsPageLocators:
    CONTACT_DETAILS_PAGE_URL: str = base_url + "contactDetails"
    CONTACT_DETAILS_FORM = (By.CSS_SELECTOR, "#contactDetails")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout")
    RETURN_BUTTON = (By.CSS_SELECTOR, "#return")
    DELETE_BUTTON = (By.CSS_SELECTOR, "#delete")
    EDIT_CONTACT_BUTTON = (By.CSS_SELECTOR, "#edit-contact")
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "#birthdate")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PHONE = (By.CSS_SELECTOR, "#phone")
    STREET_ADDRESS_1 = (By.CSS_SELECTOR, "#street1")
    STREET_ADDRESS_2 = (By.CSS_SELECTOR, "#street2")
    CITY = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#stateProvince")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postalCode")
    COUNTRY = (By.CSS_SELECTOR, "#country")


@dataclass
class EditContactPageLocators:
    EDIT_CONTACT_PAGE_URL: str = base_url + "editContact"
    EDIT_CONTACT_FORM = (By.CSS_SELECTOR, "#edit-contact")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "#birthdate")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PHONE = (By.CSS_SELECTOR, "#phone")
    STREET_ADDRESS_1 = (By.CSS_SELECTOR, "#street1")
    STREET_ADDRESS_2 = (By.CSS_SELECTOR, "#street2")
    CITY = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#stateProvince")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postalCode")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
