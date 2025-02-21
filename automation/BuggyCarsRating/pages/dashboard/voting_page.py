from base.driver_methods import DriverMethods
import utilities.create_logger as cl
import logging
import time
from pages.home.login_page import LoginPage

class VotingPage(DriverMethods):
    log = cl.create_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page = LoginPage(driver)

    _popular_make = "/html/body/my-app/div/main/my-home/div/div[1]/div/a"
    _popular_model = "/html/body/my-app/div/main/my-home/div/div[2]/div/a"
    _overall_rating = "/html/body/my-app/div/main/my-home/div/div[3]/div/a/img"
    _lamborghini_img = "/html/body/my-app/div/main/my-model/div/div[1]/div[1]/div[1]/a/img"
    _text_area = "comment"
    _vote_button = "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/div/button"
    _buggy_rating_home_button ="/html/body/my-app/header/nav/div/a"
    _next_page_button = "/html/body/my-app/div/main/my-overall/div/my-pager/div/div/a[2]"
    _previous_page_button = "/html/body/my-app/div/main/my-overall/div/my-pager/div/div/a[1]"
    _page_numbers = "/html/body/my-app/div/main/my-overall/div/my-pager/div/div/input"

    def login_user(self, login, password):
        self.login_page.valid_login(login, password)

    def click_buggy_rating_home_button(self):
        self.element_click("xpath", self._buggy_rating_home_button)

    def click_popular_make(self):
        self.element_click("xpath", self._popular_make)
        time.sleep(3)
        self.click_buggy_rating_home_button()
        time.sleep(3)

    def click_popular_model(self):
        self.element_click("xpath", self._popular_model)
        time.sleep(3)
        self.click_buggy_rating_home_button()
        time.sleep(3)

    def click_overall_rating(self):
        self.element_click("xpath", self._overall_rating)

    def choose_model(self, model):
        model_locator = f"//a[contains(text(),'{model}')]"
        self.element_click("xpath", model_locator)

    def enter_text(self, text):
        self.send_keys(text, "id", self._text_area)

    def click_vote_button(self):
        self.element_click("xpath", self._vote_button)

    def vote_shows_up(self, text):
        comment_locator = f"//td[contains(text(), '{text}')]"
        element = self.get_element("xpath", comment_locator)
        if element is not None:
            self.log.info("Comment can found: " + text)
            return True
        else:
            self.log.info("Comment can not found: " + text)
            return False

    def click_next_page(self):
        next_button = self.get_element("xpath", self._next_page_button)
        if next_button and next_button.is_enabled():
            self.element_click("xpath", self._next_page_button)
            self.log.info("Navigated to the next page.")
        else:
            self.log.error("Next button is not available.")

    def click_previous_page(self):
        previous_button = self.get_element("xpath", self._previous_page_button)
        if previous_button and previous_button.is_enabled():
            self.element_click("xpath", self._previous_page_button)
            self.log.info("Navigated to the previous page.")
        else:
            self.log.error("Previous button is not available.")

    def vote_first_page(self, model, text):
        self.click_overall_rating()
        time.sleep(3)
        self.choose_model(model)
        time.sleep(3)
        self.enter_text(text)
        time.sleep(3)
        self.click_vote_button()
        time.sleep(3)
        self.vote_shows_up(text)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,-600);")
        time.sleep(3)
        self.click_buggy_rating_home_button()
        time.sleep(3)

    def pagination_next_page(self):
        self.click_overall_rating()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,600);")
        time.sleep(3)
        self.click_next_page()
        time.sleep(3)

    def pagination_previous_page(self):
        self.click_previous_page()
        time.sleep(3)

    def vote_next_page(self, model, text):
        self.click_overall_rating()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,600);")
        time.sleep(3)
        self.click_next_page()
        time.sleep(3)
        self.choose_model(model)
        time.sleep(3)
        self.enter_text(text)
        time.sleep(3)
        self.click_vote_button()
        time.sleep(3)
        self.vote_shows_up(text)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,-600);")
        time.sleep(3)
        self.click_buggy_rating_home_button()
        time.sleep(3)


