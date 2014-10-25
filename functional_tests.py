from selenium import webdriver
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
		self.fail('finish the test!')
		



# Lets enter an item to be done

# Types in and hits return.

# Page Updates

# Enter another item

# Enters another, page updates again

# Unique URL

# visits url...list is there

# Logs off

if __name__== '__main__':
	unittest.main(warnings='ignore')
	
	
	


