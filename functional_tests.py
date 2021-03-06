from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        #sally checks the page
        self.browser.get('http://localhost:8000')
        "she notices that the page title says *Todo*"
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finnish the test!')


if __name__ == '__main__':

    unittest.main(warnings='ignore')
