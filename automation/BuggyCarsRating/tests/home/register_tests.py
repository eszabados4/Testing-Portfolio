from pages.home.register_page import RegisterPage
import unittest
import pytest

"""
Terminal: py.test -s -v tests/home/register_tests.py --browser chrome
"""

@pytest.mark.usefixtures("one_time_setup", "setup")
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.register_page = RegisterPage(self.driver)

    def test_valid_register(self):
        self.register_page.register("janetest", "Jane", "Doe", "Abcabc$123", "Abcabc$123")

