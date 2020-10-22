import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_post_creation_type(self):
        pass

    def test_post_creation_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
