from xhtml2pdf import pisa
import io as StringIO
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
import os.path


# Class that does various convertions.
class Convert:
	settings.configure()
	# Convert html to pdf
	def html_to_pdf(self, template_src, context_dict):
		try:
			template = get_template(os.path.realpath(template_src) )


			context = Context(context_dict)
			html = template.render(context)
			result = StringIO.StringIO()

			pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)

			if not pdf.err:
				return HttpResponse(result.getvalue(), content_type='application/pdf')
			else:
				return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
		except Exception as err:
			print("ERROR %s" %err)
			return "Error encountered"
