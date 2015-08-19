from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class EditorWeightTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_case(self):
		self.browser.get('http://localhost:8000')
		print (self.browser.title)
		self.assertIn('editorWeight', self.browser.title)

		inputbox = self.browser.find_element_by_id('weightInput')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter your weights'
		)

		inputbox.send_keys('100')

		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text =='1: 100' for row in rows), 
			"New weight did not appear in table"
		)

if __name__ == '__main__':
	unittest.main(warnings='ignore')