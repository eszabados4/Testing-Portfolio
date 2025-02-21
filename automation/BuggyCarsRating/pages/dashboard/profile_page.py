from base.driver_methods import DriverMethods
import utilities.create_logger as cl
import logging
import time
from pages.home.login_page import LoginPage
from selenium.webdriver.common.keys import Keys



class ProfilePage(DriverMethods):
    log = cl.create_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page = LoginPage(driver)

    #Locators
    _profile_button = "//a[text()='Profile']"
    _first_name = "firstName"
    _last_name = "lastName"
    _gender = "gender"
    _age = "age"
    _address = "address"
    _phone = "phone"
    _hobby= "hobby"
    _current_password = "currentPassword"
    _new_password = "newPassword"
    _confirm_password = "newPasswordConfirmation"
    _language = "language"
    _save_button = "//button[@type='submit']"
    _cancel_button= "//a[@role='button']"

    def login_user(self, login, password):
        self.login_page.valid_login(login, password)

    def click_profile_button(self):
        self.element_click("xpath", self._profile_button)

    def click_save_button(self):
        self.element_click("xpath", self._save_button)

    def change_first_name(self, first_name):
        self.click_profile_button()
        time.sleep(3)
        input_field = self.get_element("id", self._first_name)
        input_field.clear()
        time.sleep(3)
        self.send_keys(first_name, "id", self._first_name)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def change_last_name(self, last_name):
        self.click_profile_button()
        time.sleep(3)
        input_field = self.get_element("id", self._last_name)
        input_field.clear()
        time.sleep(3)
        self.send_keys(last_name, "id", self._first_name)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)


    def pick_gender(self, gender):
        self.click_profile_button()
        time.sleep(3)
        element = self.get_element("id", self._gender)
        self.send_keys(gender, "id", self._gender)
        time.sleep(3)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def change_gender(self, gender):
        self.click_profile_button()
        time.sleep(3)
        element = self.get_element("id", self._gender)
        element.clear()
        time.sleep(3)
        self.send_keys(gender, "id", self._gender)
        time.sleep(3)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def enter_age(self, age):
        self.click_profile_button()
        time.sleep(3)
        self.send_keys(age, "id", self._age)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def change_age(self, age):
        self.click_profile_button()
        time.sleep(3)
        element = self.get_element("id", self._age)
        element.clear()
        time.sleep(3)
        self.send_keys(age, "id", self._age)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def enter_address(self, address):
        self.click_profile_button()
        time.sleep(3)
        self.send_keys(address, "id", self._address)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def change_address(self, address):
        self.click_profile_button()
        time.sleep(3)
        element = self.get_element("id", self._address)
        element.clear()
        time.sleep(3)
        self.send_keys(address, "id", self._address)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def enter_phone(self, phone):
        self.click_profile_button()
        time.sleep(3)
        self.send_keys(phone, "id", self._phone)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def change_phone(self, phone):
        self.click_profile_button()
        time.sleep(3)
        element = self.get_element("id", self._phone)
        element.clear()
        time.sleep(3)
        self.send_keys(phone, "id", self._phone)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def pick_hobby(self, hobby):
        self.click_profile_button()
        time.sleep(3)
        hobby_locator = f"//option[contains(text(),'{hobby}')]"
        self.element_click("xpath", hobby_locator)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def change_password(self, password, new_password):
        self.click_profile_button()
        time.sleep(3)
        self.send_keys(password, "id", self._current_password)
        time.sleep(3)
        self.send_keys(new_password, "id", self._new_password)
        time.sleep(3)
        self.send_keys(new_password, "id", self._confirm_password)
        time.sleep(3)
        self.click_save_button()
        time.sleep(3)

    def cancel_profile_page(self):
        self.click_profile_button()
        time.sleep(3)
        self.element_click("xpath", self._cancel_button)
        time.sleep(3)

