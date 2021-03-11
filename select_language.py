import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        exp_option = ['English', 'French', 'German']
        active_options = []

        select_language = Select(
            self.driver.find_element_by_id('select-language'))

        self.assertEqual(len(exp_option), len(select_language.options))

        for option in select_language.options:
            active_options.append(option.text)

        self.assertListEqual(exp_option, active_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(
            self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
