from pages.home.login_page import LoginPage
import unittest
import pytest

from tests.conftest import *

"""
Terminal: py.test -s -v tests/home/register_tests.py tests/home/login_tests.py --browser chrome
Terminal: py.test -s -v tests/home/login_tests.py --browser chrome
"""

@pytest.mark.usefixtures("setup","one_time_setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.run(order=5)
    def test_valid_login(self):
        self.login_page.valid_login("janetest", "Abcabc$123")

    @pytest.mark.run(order=1)
    def test_login_with_invalid_login(self):
        self.login_page.invalid_login("jane", "Abcabc$123")

    @pytest.mark.run(order=2)
    def test_login_with_invalid_password(self):
        self.login_page.invalid_login("janetest", "Abcabc")

    @pytest.mark.run(order=3)
    def test_login_with_empty_login(self):
        self.login_page.invalid_login("", "Abcabc$123")

    @pytest.mark.run(order=4)
    def test_login_with_empty_password(self):
        self.login_page.invalid_login("janetest", "")