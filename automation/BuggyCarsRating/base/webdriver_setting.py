from selenium import webdriver


class WebdriverSetting:

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        base_url = "https://buggy.justtestit.org/"

        if self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)

        return driver