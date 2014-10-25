from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		# Title and header mention to do lists
		self.assertIn('To-Do',  self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		
		# Lets enter an item to be done
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item' )
		# Types " Buying peacock feathers" in and hits return.
		inputbox.send_keys('Buy peacock feathers')

		# Page Updates

		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))
		


# Enter another item
		self.fail('finish the test!')

# Enters another, page updates again

# Unique URL

# visits url...list is there

# Logs off

if __name__== '__main__':
	unittest.main(warnings='ignore')
	
	
	


