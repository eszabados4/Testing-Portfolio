from pages.dashboard.profile_page import ProfilePage
import unittest
from tests.conftest import *
import pytest


"""
Terminal: py.test -s -v tests/dashboard/profile_tests.py  --browser chrome

"""

@pytest.mark.usefixtures("setup", "one_time_setup")
class ProfileTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.login_user("janetest", "Abcabc$123")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_first_name(self):
        self.profile_page.change_first_name("Mary")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_last_name(self):
        self.profile_page.change_last_name("Smith")

    @pytest.mark.skip(reason="Not relevant")
    def test_pick_gender(self):
        self.profile_page.pick_gender("Female")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_gender(self):
        self.profile_page.change_gender("Male")

    @pytest.mark.skip(reason="Not relevant")
    def test_enter_age(self):
        self.profile_page.enter_age("26")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_age(self):
        self.profile_page.change_age("32")

    @pytest.mark.skip(reason="Not relevant")
    def test_enter_address(self):
        self.profile_page.enter_address("1000 City Abc Street 2.")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_address(self):
        self.profile_page.change_address("2500 Village Long Street 56.")

    @pytest.mark.skip(reason="Not relevant")
    def test_enter_phone(self):
        self.profile_page.enter_phone("00123456789")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_phone(self):
        self.profile_page.change_phone("00987654321")

    @pytest.mark.skip(reason="Not relevant")
    def test_pick_hobby(self):
        self.profile_page.pick_hobby("Jogging")

    @pytest.mark.skip(reason="Not relevant")
    def test_change_password(self):
        self.profile_page.change_password("Abcabc$123", "Testpw+555")

    @pytest.mark.skip(reason="Not relevant")
    def test_cancel_profile_page(self):
        self.profile_page.cancel_profile_page()


