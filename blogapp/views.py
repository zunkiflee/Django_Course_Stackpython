from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import *
from django.db.models import Q
import csv
from .forms import *



def home(request):
	search_post = request.GET.get('search')
	print(search_post)

	if search_post:
		posts = Blog.objects.filter(Q(title__contains=search_post) & Q(post__contains=search_post))
	else:
		posts = Blog.objects.all()

	context = {'posts':posts}
	return render(request, "blogapp/home.html",context)


def about(request):
	return render(request, "blogapp/about.html")


def post_details(request, id):
	single_post = Blog.objects.get(pk=id)
 
	context = {'single_post':single_post}
	return render(request, 'blogapp/postdetails.html', context)


def table(request):
	table_obj = Blog.objects.all()
	context = {'table_obj':table_obj}

	return render(request, 'blogapp/table.html', context)


def export_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="blog.csv"'

	writer = csv.writer(response)
	writer.writerow(['Column1', 'Column2', 'Column3'])

	# query select headers
	post_obj = Blog.objects.all().values_list('title', 'date_created', 'date_updated')
	
	# Finally, iterate fields, and put qerried data
	for po in post_obj:
		writer.writerow(po)

	return response


def contact(request):
	form = ContactForm()

	if request.method == 'POST':
		print('This is POST')
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('home-page')
	else:
		print('This is GET')
		form = ContactForm

	context = {'form':form}

	return render(request, 'blogapp/forms.html', context)

def thak(request):
	return HttpResponse("Thank you for submit")


def test(request):

	# query all object
	posts = Blog.objects.all().reverse()
	#query one obnect
	#posts = Blog.objects.get(pk=1)

	#limit query
	#posts = Blog.objects.all()[:2]

	# Reverse
	#posts = Blog.objects.order_by('-id')

	#get only sepcific fields
	#posts = Blog.objects.values('title', 'id', 'post')

	#get the first object
	#posts2 = Blog.objects.first()

	#get the last object
	#posts3 = Blog.objects.last()

	context  = {'posts':posts}
	
	return render(request, "blogapp/test.html", context)




