from django.shortcuts import render
from .models import *

def home(request):
	return render(request,'kapp/home.html')


def search(request):
	query = request.GET['q']
	searched_courses = list()

	if query:
		raw_courses = Courses.objects.raw('SELECT id , title , MATCH (title,details ) AGAINST ( "' + query + '" ) AS score FROM courses WHERE MATCH (title,details) AGAINST ( "' + query +'") ORDER BY score DESC,length(title);')
		for course in raw_courses:
			if course.score >= 5:
				searched_courses.append(course)
	else:
		return render(request,'kapp/search.html',{'error' : 'Please search something, bro!'})
		
	if not searched_courses:
		return render(request,'kapp/search.html',{'error' : 'No results found!'})
	return render(request,'kapp/search.html',{'Courses' : searched_courses})