import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import keys

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_keyword_search(self):
        driver = self.driver
        driver.get('http://www.google.com/')
        
        # check page title
        assertEqual(d.title, 'Google')

        # pass keyword to serach box
        elem_text = d.find_element_by_id('lst-ib')
        elem_text.send_keys('python course')

        # click submit button and see output
        elem_bt = d.find_element_name('btnG').click()

        # try another string, but first clear text
        elem_text.clear()
        elem_text.send_keys('restaurant san jose')

        # click to see results
        elem_bt = d.find_element_name('btnG').click()
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
