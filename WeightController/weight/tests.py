from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from weight.views import editorWeight
from weight.models import Weight

class EditorWeightTest(TestCase):
	def test_url(self):
		editorWeightPage = resolve('/')
		self.assertEqual(editorWeightPage.func, editorWeight)

	def test_response_html(self):
		request = HttpRequest()
		response = editorWeight(request)

		expected_html = render_to_string('editorWeight.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_save_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['weightInput'] = '50'

		response = editorWeight(request)
		self.assertIn('50', response.content.decode())

		expected_html = render_to_string(
			'editorweight.html',
			{'new_weight': '50'}
		)
		print (expected_html)
		self.assertEqual(response.content.decode(), expected_html)

class WeightModelTest(TestCase):

	def test_save_weight(self):
		weight1 = Weight()
		weight1.weight = "100"
		weight1.save()

		weight2 = Weight()
		weight2.weight = "50"
		weight2.save()

		saved_weights = Weight.objects.all()
		self.assertEqual(saved_weights.count(), 2)

		weight1 = saved_weights[0]
		weight2 = saved_weights[1]
		self.assertEqual(weight1.weight, "100")
		self.assertEqual(weight2.weight, "50")