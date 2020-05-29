from django.shortcuts import render
import os
from django.http import HttpResponse, Http404
from django.contrib.staticfiles import finders

# Create your views here.
def resume(request):
    return render(request, 'resume.html', {})

def home(request):
    return render(request, 'home.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def download_resume(request):
	file_path = finders.find('docs/JESMAN_DZIMBA_RESUME.pdf')

	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/pdf")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404

def new_header(request):
	return render(request, 'new_header.html', {})


# download_resume()
