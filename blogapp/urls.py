from django.urls import path
from .views import *



urlpatterns = [
	path('', home, name='home-page'),
	path('about/', about, name='about-page'),
	path('test/', test, name='test-page'),
	path('post-details/<int:id>', post_details, name="post-details"),
	path('table/', table, name="table-page"),
	path('export-csv/', export_csv, name="export-page"),
	path('contact/', contact, name="form-page"),
	path('thak/', thak, name="thak-page"),
]



