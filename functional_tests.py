
from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:8000')
#assert 'Laura' in browser.title, "Browser title was "+ browser.title

import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # She notices the page title and header mention CV section lists

        #headerText = self.browser.find_element_by_tag_name('h2').text;
        #print("header text" + headerText)
        #self.assertTrue("Text not found!", "CV" in headerText);

        self.assertTrue("testedesdsd" in self.browser.page_source);

        #self.assertIn('To-Do', self.browser.title)  
        #self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away
        #[...rest of comments as before]

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  