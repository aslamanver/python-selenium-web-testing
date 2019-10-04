from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time 


class KithunuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver_75')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://material.angular.io/components/select/examples")

    def test_signup(self):

        time.sleep(1)
        
        # self.driver.find_element_by_xpath("//mat-select[@id='mat-select-0']").click()
        self.driver.find_element_by_xpath("//mat-select[contains(@id, 'mat-select-0')]").click()
        self.driver.find_element_by_xpath("//mat-option[contains(@class, 'mat-option') and contains(.//span, 'Pizza')]").click()
        
        self.driver.find_element_by_xpath("//mat-select[contains(@id, 'mat-select-1')]").click()
        self.driver.find_element_by_xpath("//mat-option[contains(@class, 'mat-option') and contains(.//span, 'Option 1')]").click()

        # self.driver.find_element_by_xpath("//mat-select[@id='mat-select-0']").click()
        # self.driver.find_element_by_xpath("//mat-option[@id='mat-option-0']").click()
        # self.driver.find_element_by_id('mat-option-0').click()
        
        # self.driver.find_element_by_xpath("//mat-select[@id='mat-select-0']").click()
        # self.driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/mat-option[text()[normalize-space(.)='Pizza']]").click()

        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Basic mat-select'])[1]/following::span[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Steak'])[1]/following::span[1]").click()

        self.assertTrue('Select' in self.driver.title)

    def tearDown(self):
        pass
        # self.driver.quit()


if __name__ == '__main__':
    unittest.main()
