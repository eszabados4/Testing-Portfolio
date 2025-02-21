from base.driver_methods import DriverMethods
import utilities.create_logger as cl
import logging
import time

class LoginPage(DriverMethods):
    log = cl.create_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_input_field = "//input[@name='login']"
    _password_input_field = "//input[@name='password']"
    _login_button = "//button[@type='submit']"


    def enter_login(self, login):
        self.send_keys(login, "xpath", self._login_input_field)

    def enter_password(self, password):
        self.send_keys(password, "xpath", self._password_input_field)

    def click_login_button(self):
        self.element_click("xpath", self._login_button)


    def clear_input_fields(self):
        login_field = self.get_element("xpath", self._login_input_field)
        login_field.clear()

        password_field = self.get_element("xpath", self._password_input_field)
        password_field.clear()

    def valid_login(self, login="", password=""):
        self.enter_login(login)
        time.sleep(3)
        self.enter_password(password)
        time.sleep(3)
        self.click_login_button()
        time.sleep(3)


    def invalid_login(self, login="", password=""):
        self.enter_login(login)
        time.sleep(3)
        self.enter_password(password)
        time.sleep(3)
        self.click_login_button()
        time.sleep(3)
        self.clear_input_fields()
        time.sleep(3)