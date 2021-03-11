import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_twitter(self):
        self.driver.get('https://twitter.com/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    testRunner = HTMLTestRunner(output='./', report_name='hello-world-report')
    unittest.main(verbosity=2, testRunner=testRunner)
