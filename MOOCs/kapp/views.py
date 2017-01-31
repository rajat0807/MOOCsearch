from django.shortcuts import render
from .models import *

def home(request):
	return render(request,'kapp/home.html')


def search(request):
	query = request.GET['q']

	if query:
		searched_courses = Courses.objects.filter(title__icontains=query)
	else:
		return render(request,'kapp/search.html',{'error' : 'Please search something, bro!'})

	print(searched_courses)

	if len(searched_courses) == 0:
		return render(request,'kapp/search.html',{'error' : 'No results found!'})
	return render(request,'kapp/search.html',{'Courses' : searched_courses})