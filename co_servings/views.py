


from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.




def home(request):
	return render(request, 'co_servings/home.html')


def how(request):
	return render(request, 'co_servings/how.html')

def white(request):
	return render(request, 'co_servings/white.html')


def liquiditypools(request):
	liquiditypools = Liquidity_Pool.objects.all()

	
	return render(request, 'co_servings/liquiditypools.html', {'liquidity': liquiditypools})


def projects(request):
	projects = Project.objects.all()
	
	
	return render(request, 'co_servings/projects.html', {'list': projects})

def webinvestors(request):
	webinvestors = Webinvestor.objects.all()
	projects = Project.objects.all()
	investments = Investment.objects.all()


	context = {'webinvestors': webinvestors, 'list':projects, 'name':webinvestors, 'project': investments}
	return render(request, 'co_servings/webinvestors.html', context)

def development(request):
	
	return render(request, 'co_servings/development.html')

def rental(request):
	return render(request, 'co_servings/rental.html')