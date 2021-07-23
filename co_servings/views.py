from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def home(request):
	return render(request, 'co_servings/home.html')

def projects(request):
	projects = Project.objects.all()
	return render(request, 'co_servings/projects.html', {'list': projects})

def webinvestors(request):
	projects = Project.objects.all()
	return render(request, 'co_servings/webinvestors.html', {'list': projects})