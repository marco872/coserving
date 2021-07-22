from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'co_servings/home.html')

def projects(request):
	return render(request, 'co_servings/projects.html')

def webinvestors(request):
	return render(request, 'co_servings/webinvestors.html')