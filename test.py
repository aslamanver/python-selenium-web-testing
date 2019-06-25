from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# browser = webdriver.Chrome('./chromedriver_75')
# browser.get('http://www.google.com')
# assert 'Google' in browser.title
# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# browser.quit()

class SearchText(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome('./chromedriver_75')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):

        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()
        self.assertTrue ('Selenium' in self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()