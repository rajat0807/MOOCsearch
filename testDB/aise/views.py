from django.shortcuts import render
from models import Details
import os
import json
import Levenshtein

def index(request):
	json_data = open('aise/static/courses.json')
	data = json.load(json_data)
	context = {'data' : data}
	return render(request,'aise/index.html',context)

