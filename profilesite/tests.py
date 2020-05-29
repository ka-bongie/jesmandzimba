from django.test import TestCase
from classes import Converter
import os.path


# Create your tests here.
class ConverterTestCase(TestCase):

	def test_html_template_converted_to_pdf(self):
		template_src = 'templates\\resume.html'
		self.assertTrue(os.path.exists(template_src))
		self.assertTrue( os.path.exists(template_src) )

		context_dict =  {'pagesize':'A4'}
		convert = Converter.Convert()
		convert.html_to_pdf(template_src, context_dict)



jes = ConverterTestCase()
jes.test_html_template_converted_to_pdf()
