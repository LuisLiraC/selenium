import unittest
from selenium import webdriver
from time import sleep


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_to_add = int(input('How many elements will you add?'))
        elements_to_remove = int(input('How many elements will you remove?'))
        total_elements = elements_to_add - elements_to_remove

        add_button = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/button')

        sleep(3)

        for i in range(elements_to_add):
            add_button.click()

        for i in range(elements_to_remove):
            try:
                delete_button = driver.find_element_by_class_name(
                    'added-manually')
                delete_button.click()
            except:
                print('You\'re trying to delete more elements than the existent')
                break

        if total_elements > 0:
            print(f'There are {total_elements} elements')
        else:
            print('There are 0 elements')

        sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
