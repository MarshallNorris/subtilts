from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # User goes to homepage
        self.browser.get('http://localhost:8000')
        
        # User sees page title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # User is invited to enter a to-do item
        
        # User types "Buy peacock feathers" into text box
        
        # User hits enter and page updates, displaying
        # "1: Buy peacock feathers"
        
        # Still a text box so user enters "Use peacock feathers to make a fly"
        
        # Page updates, shows both items
        
        # Site has generated unique URL for list and explains that it has
        
        # User goes to URL, her to-do list is there
        
        # User leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')
browser.quit()
