from django.shortcuts import render
from .models import *

def home(request):
	return render(request,'kapp/home.html')


def search(request):
	query = request.GET['q']
	print("Requested query : "+str(query))

	if query:
		words = query.split()
		cour = Coursera.objects.filter(title__icontains=query)
		infy = Infy.objects.filter(title__icontains=query)
		lynda = Lynda.objects.filter(title__icontains=query)
		nptel = Nptel.objects.filter(title__icontains=query)
		udac = Udacity.objects.filter(title__icontains=query)

	else:
		return render(request,'kapp/search.html',{'error' : 'Please search something, bro!'})


	print(infy)
	return render(request,'kapp/search.html',{'Coursera' : cour, 'Infy': infy, 'Lynda': lynda, 'NPTEL' : nptel, 'Udacity' : udac,})