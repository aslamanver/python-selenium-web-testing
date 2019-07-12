
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class SearchText(unittest.TestCase):
     
    def setUp(self):

        self.driver = webdriver.Chrome('./chromedriver_75')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://localhost/kithunu-app-mobile/signup")

    def test_signup(self):

        first_name = self.driver.find_element_by_id("mat-input-0")
        first_name.send_keys("Aslam")

        last_name = self.driver.find_element_by_id("mat-input-1")
        last_name.send_keys("Anver")

        self.assertTrue ('KithunuAppMobile' in self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()