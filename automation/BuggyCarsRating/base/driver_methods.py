from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.create_logger as cl
import logging
from selenium.webdriver.support.select import Select


class DriverMethods:

    log = cl.create_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_locator_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.error("Locator type: "+ locator_type + "not correct")
        return False

    def get_element(self, locator_type, locator):
        element = None
        locator_type = locator_type.lower()
        try:
            selected_locator_type = self.get_locator_type(locator_type)
            element = self.driver.find_element(selected_locator_type,locator)
            self.log.info("Element found with locator type: " + locator_type + " and locator: " + locator)
        except:
            self.log.error("Element  not found with locator type: " + locator_type + " and locator: " + locator)
            print_stack()
        return element

    def element_click(self, locator_type, locator):
        try:
            element = self.get_element(locator_type,locator)
            element.click()
            self.log.info("Clicked on element with locator type:" + locator_type + "locator:" + locator)
        except:
            self.log.error("Can not click on element with locator type:" + locator_type + "locator:" + locator)
            print_stack()

    def send_keys(self, data, locator_type, locator):
        try:
            element = self.get_element(locator_type,locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator type:" + locator_type + "locator:" + locator)
        except:
            self.log.error("Can not send data on element with locator type:" + locator_type + "locator:" + locator)
            print_stack()

    def wait_for_element(self, locator_type, locator, timeout=10, poll_frequency=0.5):
        element = None
        try:
            selected_locator_type = self.get_locator_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout,poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                      ElementNotVisibleException,
                                                      ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((selected_locator_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def element_presence_check(self, locator_type, locator):
        try:
            element = self.get_element(locator_type,locator)
            if element is not  None:
                self.log.info("Element found")
                return  True
            else:
                self.log.info("Element not found")
                return  False
        except:
            self.log.info("Element not found")
            return False

    def select_dropdown_with_value(self, locator_type, locator, value):
        try:
            locator_type = locator_type.lower()
            selected_locator_type = self.get_locator_type(locator_type)
            element = self.driver.find_element(selected_locator_type, locator)
            sel = Select(element)
            sel.select_by_value(value)
            self.log.info("Value: " + value + "from dropdown list found")
        except:
            self.log.error("Value: " + value + "from dropdown list not found")

