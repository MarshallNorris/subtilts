from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # User is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        
        # User types "Buy peacock feathers" into text box
        inputbox.send_keys('Buy peacock feathers')        

        # User hits enter and page updates, displaying
        # "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_elemnt_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Still a text box so user enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
        
        # Page updates, shows both items
        
        # Site has generated unique URL for list and explains that it has
        
        # User goes to URL, her to-do list is there
        
        # User leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')
browser.quit()
