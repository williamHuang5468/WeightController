from selenium import webdriver
import unittest

class EditorWeightTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_case(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('editorWeight', self.browser.title)

if __name__ == '__main__':
	unittest.main(warnings='ignore')