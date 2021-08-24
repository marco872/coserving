


from django.shortcuts import render 
from django.http import HttpResponseRedirect

from .models import *

from .forms import VenueForm, LiquidityForm

# Create your views here.







def home(request):
	return render(request, 'co_servings/home.html')


def how(request):
	return render(request, 'co_servings/how.html')

def white(request):
	return render(request, 'co_servings/white.html')


def liquiditypools(request):
	liquidity = Liquidity.objects.all()
	
	starting = liquidity.count()
	filling_up = liquidity.filter(status='Filling_up').count()
	completed = liquidity.filter(status='Completed').count()
	
	context = {'topic': liquidity, 'starting':starting, 'filling_up':filling_up, 'completed':completed}
	return render(request, 'co_servings/liquiditypools.html', context )

def venue(request):
	submitted = False
	form = VenueForm()
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/venue?submitted=True')

	else:
		form = VenueForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/venue.html', {'form':form, 'submitted':submitted })




def projects(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()

	context = {'list': projects, 'value': venue}
	return render(request, 'co_servings/projects.html',context )

def liquidity(request):
	submitted = False
	form = LiquidityForm()
	if request.method == "POST":
		form = LiquidityForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/liquidity?submitted=True')

	else:
		form = LiquidityForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/liquidity.html', {'form':form, 'submitted':submitted })





def webinvestors(request):
	webinvestors = Webinvestor.objects.all()
	projects = Project.objects.all()
	investments = Investment.objects.all()


	context = {'webinvestors': webinvestors, 'list':projects, 'name':webinvestors, 'project': investments}
	return render(request, 'co_servings/webinvestors.html', context)

def development(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()
	liquidity = Liquidity.objects.all()

	context = {'list': projects, 'value': venue, 'topic': liquidity}
	return render(request, 'co_servings/development.html',context )
	
	return render(request, 'co_servings/development.html')

def rental(request):
	return render(request, 'co_servings/rental.html')

