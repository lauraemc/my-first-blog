
from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:8000')
#assert 'Laura' in browser.title, "Browser title was "+ browser.title

import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()#driver
        
    def tearDown(self):  
        self.browser.quit()

    def test_can_view_whole_cv(self):  
        # User is able to log onto site
        self.browser.get('http://127.0.0.1:8000')

        # User able to view CV section on main page
        self.assertTrue("My CV" in self.browser.page_source);

        # User able to view every CV section on main page

        cvSections = ["Work Summary", "Volunteering", "Education","Technical Skills","Extracurricular"]
        for section in cvSections:
            self.assertTrue(section in self.browser.page_source);

        #loginLink = self.browser.findElement(By.linkText("Work Summary"));
        #heading1 = self.browser.find_element_by_tag_name('h1').text
        #self.assertTrue("Work Summary" in heading1)
        #h1 = self.browser.find_element_by_xpath('/h1/[text()="Work Summary"]')
        #self.assertTrue(selenium.isElementPresent("//H2[.='Work Summary']"));

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  