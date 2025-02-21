from pages.dashboard.voting_page import VotingPage
import unittest
from tests.conftest import *
import pytest

"""
Terminal: py.test -s -v tests/dashboard/voting_tests.py  --browser chrome

"""
@pytest.mark.usefixtures("setup", "one_time_setup")
class VotingTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, one_time_setup):
        self.voting_page = VotingPage(self.driver)
        self.voting_page.login_user("janetest", "Abcabc$123")

    def test_click_popular_make(self):
        self.voting_page.click_popular_make()

    def test_click_popular_model(self):
        self.voting_page.click_popular_model()

    def test_vote_first_page(self):
        self.voting_page.vote_first_page("Zonda", "This is a vote")

    @pytest.mark.skip(reason="Already tested")
    def test_pagination_next(self):
        self.voting_page.pagination_next_page()

    @pytest.mark.skip(reason="Already tested")
    def test_pagination_previous(self):
        self.voting_page.pagination_previous_page()

    def test_vote_next_page(self):
        self.voting_page.vote_next_page("Veneno", "This is a vote")


