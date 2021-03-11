import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed()
                        and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        driver.implicitly_wait(1)
        middle_name = driver.find_element_by_id('middlename')
        driver.implicitly_wait(1)
        last_name = driver.find_element_by_id('lastname')
        driver.implicitly_wait(1)
        email_address = driver.find_element_by_id('email_address')
        driver.implicitly_wait(1)
        newsletter_suscription = driver.find_element_by_id('is_subscribed')
        driver.implicitly_wait(1)
        password = driver.find_element_by_id('password')
        driver.implicitly_wait(1)
        confirm_password = driver.find_element_by_id('confirmation')
        driver.implicitly_wait(1)
        submit_button = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and newsletter_suscription.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys('Test')
        middle_name.send_keys('Selenium')
        last_name.send_keys('Platzi')
        email_address.send_keys('googleboy@testinggmail.com')
        password.send_keys('eltimoti')
        confirm_password.send_keys('eltimoti')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
