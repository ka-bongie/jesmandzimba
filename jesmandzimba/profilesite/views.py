from django.shortcuts import render

# Create your views here.
def resume(request):
    return render(request, 'resume.html', {})

def home(request):
    return render(request, 'home.html', {})
