"""jesmandzimba URL Configuration

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('resume', views.resume, name="resume"),
	path('portfolio', views.portfolio, name="portfolio"),
	path('resume/download', views.download_resume, name="download_resume"),
]
