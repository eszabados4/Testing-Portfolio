from base.webdriver_setting import WebdriverSetting
import pytest
import utilities.create_logger as cl
import logging

log = cl.create_logger(logging.DEBUG)


@pytest.fixture()
def setup():
    log.info("Running method level setUp")
    yield
    log.info("Running method level tearDown")

@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    webdriver = WebdriverSetting(browser)
    driver = webdriver.get_webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    log.info("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
