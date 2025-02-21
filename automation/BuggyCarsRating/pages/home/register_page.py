from base.driver_methods import DriverMethods
import utilities.create_logger as cl
import logging
import time

class RegisterPage(DriverMethods):

    log = cl.create_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _register_button = "/html/body/my-app/header/nav/div/my-login/div/form/a"  # "Register" linktext
    _login_field = "username" # id
    _first_name_field = "firstName" # id
    _last_name_field = "lastName" # id
    _password_field = "password" # id
    _confirm_password_field = "confirmPassword"  # id
    _submit_register_button = "/html/body/my-app/div/main/my-register/div/div/form/button"
    _cancel_button = "/html/body/my-app/div/main/my-register/div/div/form/a"


    #Actions
    def click_register_button(self):
        self.element_click("xpath", self._register_button)

    def enter_login(self, login):
        self.send_keys(login, "id", self._login_field)

    def enter_first_name(self, first_name):
        self.send_keys(first_name, "id", self._first_name_field)

    def enter_last_name(self, last_name):
        self.send_keys(last_name, "id", self._last_name_field)

    def enter_password_1(self, password_1):
        self.send_keys(password_1, "id", self._password_field)

    def enter_password_2(self, password_2):
        self.send_keys(password_2, "id", self._confirm_password_field)

    def click_submit_register_button(self):
        self.element_click("xpath", self._submit_register_button)

    def click_cancel_button(self):
        self.element_click("xpath", self._cancel_button)

    def register(self, login="", first_name="", last_name="", password_1="", password_2=""):
        self.click_register_button()
        time.sleep(3)
        self.enter_login(login)
        time.sleep(3)
        self.enter_first_name(first_name)
        time.sleep(3)
        self.enter_last_name(last_name)
        time.sleep(3)
        self.enter_password_1(password_1)
        time.sleep(3)
        self.enter_password_2(password_2)
        time.sleep(3)
        self.click_submit_register_button()
        time.sleep(3)




