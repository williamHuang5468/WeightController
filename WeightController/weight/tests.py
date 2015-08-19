from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from weight.views import editorWeight

class EditorWeightTest(TestCase):
	def test_url(self):
		editorWeightPage = resolve('/')
		self.assertEqual(editorWeightPage.func, editorWeight)

	def response_html(self):
		request = HttpRequest()
		response = home(request)
		
		self.assertTrue(response.startswith(b"<html>"))
		self.assertIn(b'<title>editorWeight</title>', response.content)
		self.assertTrue(response.startswith(b"</html>"))