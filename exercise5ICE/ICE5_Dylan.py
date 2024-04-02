# Filename: ICE5_Dylan
# Name: Dylan Gill
# Date: April 2, 2024
# Description: Test cases for user registration and login functionality.
#

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ICE5inclass_Dylan import TestReglog

class TestRegistration(unittest.TestCase):
        def setUp(cls):
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(10)  
            cls.driver.maximize_window()

        def tearDown(cls):
            cls.driver.quit()

        def test_registration(self):
            # Testcase to register a new user
            self.driver.get("https://demo.guru99.com/test/newtours/")
            self.driver.set_window_size(974, 1032)

            # Clicking on the "REGISTER" link to navigate to the page
            self.driver.find_element(By.LINK_TEXT, "REGISTER").click()

            # Filling out registration form with user details
            self.driver.find_element(By.NAME, "firstName").click()
            self.driver.find_element(By.NAME, "firstName").send_keys("Dylan")
            self.driver.find_element(By.NAME, "lastName").send_keys("Gill")
            self.driver.find_element(By.NAME, "phone").send_keys("9051231988")
            self.driver.find_element(By.ID, "userName").send_keys("dylangill@hotmail.com")
            self.driver.find_element(By.NAME, "address1").send_keys("123 juliet road")
            self.driver.find_element(By.NAME, "city").send_keys("Oshawa")
            self.driver.find_element(By.NAME, "state").send_keys("Ontario")
            self.driver.find_element(By.NAME, "postalCode").send_keys("L1R 1W2")

            # Selecting the country from the dropdown bar
            self.driver.find_element(By.NAME, "country").click()
            dropdown = self.driver.find_element(By.NAME, "country")
            dropdown.find_element(By.XPATH, "//option[. = 'CANADA']").click()

            # Filling out what is remaining blank on the forum
            self.driver.find_element(By.ID, "email").click()
            self.driver.find_element(By.ID, "email").send_keys("dylanthethrill")
            self.driver.find_element(By.NAME, "password").send_keys("school")
            self.driver.find_element(By.NAME, "confirmPassword").send_keys("school")

            # Submitting the registration form
            self.driver.find_element(By.NAME, "submit").click()

        def test_login_assertion(self):
            # Test case to log in with users registration credentials and assert the login, as long as registration is succesful

            self.driver.get("https://demo.guru99.com/test/newtours/")

            # Clicking on the "SIGN-ON" page
            self.driver.find_element(By.LINK_TEXT, "SIGN-ON").click()

            # Entering in username and password
            self.driver.find_element(By.NAME, "userName").click()
            self.driver.find_element(By.NAME, "userName").send_keys("dylanthethrill")
            self.driver.find_element(By.NAME, "password").send_keys("school")

            # Submit the login form
            self.driver.find_element(By.NAME, "submit").click()

            # Assering succeful login by checking for "Login Successfully" text on the page
            assert "Login Successfully" in self.driver.page_source

if __name__ == "__main__":
    unittest.main()