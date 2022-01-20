


from django.shortcuts import render 
from django.http import HttpResponseRedirect

from .models import *

from .forms import VenueForm, LiquidityForm, CollateralForm

# Create your views here.







def home(request):
	return render(request, 'co_servings/home.html')

def fbm(request):
	return render(request, 'co_servings/fbm.html')

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






def development(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()
	liquidity = Liquidity.objects.all()

	context = {'list': projects, 'value': venue, 'topic': liquidity}
	return render(request, 'co_servings/development.html',context )
	
	

def rental(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()

	context = {'list': projects, 'value': venue}
	return render(request, 'co_servings/rental.html',context )

	

def buildings(request):
	return render(request, 'co_servings/buildings.html')

def plan(request):
	return render(request, 'co_servings/plan.html')

def stand(request):
	return render(request, 'co_servings/stand.html')

def token(request):
	return render(request, 'co_servings/token.html')

def guest(request):
	return render(request, 'co_servings/guest.html')

def information1(request):
	return render(request, 'co_servings/information1.html')

def information2(request):
	return render(request, 'co_servings/information2.html')

def hostingrules(request):
	return render(request, 'co_servings/hostingrules.html')

def vaccineprotocol1(request):
	return render(request, 'co_servings/vaccineprotocol1.html')

def vaccineprotocol2(request):
	return render(request, 'co_servings/vaccineprotocol2.html')

def rentreduction(request):
	return render(request, 'co_servings/rentreduction.html')

def tokenprogram1(request):
	return render(request, 'co_servings/tokenprogram1.html')

def tokenprogram2(request):
	return render(request, 'co_servings/tokenprogram2.html')




def rentopportunity(request):

	projects = Project.objects.all()
	venue = Venue.objects.all()

	context = {'list': projects, 'value': venue}
	
	return render(request, 'co_servings/rentopportunity.html',context )







def ourcommunity1(request):
	return render(request, 'co_servings/ourcommunity1.html')

def ourcommunity2(request):
	return render(request, 'co_servings/ourcommunity2.html')

def development1(request):
	return render(request, 'co_servings/development1.html')

def overview1(request):
	return render(request, 'co_servings/overview1.html')

def overview2(request):
	return render(request, 'co_servings/overview2.html')

def guestrules(request):
	return render(request, 'co_servings/guestrules.html')

def costtrasparency(request):
	return render(request, 'co_servings/costtrasparency.html')

def guestopportunity(request):
	return render(request, 'co_servings/guestopportunity.html')

def reservation(request):
	return render(request, 'co_servings/reservation.html')

def payment1(request):
	return render(request, 'co_servings/payment1.html')

def payment2(request):
	return render(request, 'co_servings/payment2.html')

def trading(request):
	return render(request, 'co_servings/trading.html')

def investorsrules(request):
	return render(request, 'co_servings/investorsrules.html')

def tradingclarity(request):
	return render(request, 'co_servings/tradingclarity.html')

def tokenprogram3(request):
	return render(request, 'co_servings/tokenprogram3.html')

def tradingdesk(request):
	return render(request, 'co_servings/tradingdesk.html')

def ourcommunity3(request):
	return render(request, 'co_servings/ourcommunity3.html')

def report(request):
	return render(request, 'co_servings/report.html')

def news(request):
	return render(request, 'co_servings/news.html')

def owner(request):
	return render(request, 'co_servings/owner.html')






def collateral(request):
	submitted = False
	form = CollateralForm()
	if request.method == "POST":
		form = CollateralForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/collateral?submitted=True')

	else:
		form = CollateralForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/collateral.html', {'form':form, 'submitted':submitted })



def gov(request):
	collaterals = Collateral.objects.all()
	

	context = {'list': collaterals }
	return render(request, 'co_servings/gov.html',context )