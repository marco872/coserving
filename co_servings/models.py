
from django.db import models





# Create your models here.
class Home(models.Model):
	re_description = models.TextField()
	how_description = models.TextField()
	users_description = models.TextField()


class Webinvestor(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Project(models.Model):
	CATEGORY = (
		('Guestroom', 'Guestroom'),
		('Display area', 'Display area'),
		('Working station', 'Working station'),
		('Office', 'Office'),
		('Noursing room', 'Nursing room'),
		('Food corner', 'Food corner'),
		)
	owner = models.CharField(max_length=200, null=True)
	property_price = models.FloatField(null=True)
	location = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	building = models.CharField(max_length=200, null=True) #building cost+design+documentation and approval
	total_project_price = models.FloatField(null=True) #project price+building price
	
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	
	def __str__(self):
		return self.location

	
	
	
#NOT IN USE
class Liquidity_Pool(models.Model):

	STATUS = (
		('Starting', 'Starting'),
		('Filling-up', 'Filling-up'),
		('Completed', 'Completed'),
		)
	topic = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	smart_contracts = models.TextField( blank=True, null=True)

	def __str__(self):
		return self.name

	



class Investment(models.Model):
	webinvestor = models.ForeignKey(Webinvestor, null=True, on_delete= models.SET_NULL)
	liquidity_pool = models.ForeignKey(Liquidity_Pool, null=True, on_delete= models.SET_NULL)
	project = models.ForeignKey(Project, null=True, on_delete= models.SET_NULL)
	

class Development(models.Model):

	location = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True)
	plp = models.CharField(max_length=200, null=True)
	
	
	project = models.CharField(max_length=200, null=True)
	projcost = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.location

	
	
	
class Venue(models.Model):

	CATEGORY = (
		('Guestroom', 'Guestroom'),
		('Display area', 'Display area'),
		('Working station', 'Working station'),
		('Office', 'Office'),
		('Noursing room', 'Nursing room'),
		('Food corner', 'Food corner'),
		)
	owner = models.CharField(max_length=200, blank=True, null=True)
	property_price = models.CharField(max_length=200, blank=True, null=True)
	location = models.CharField(max_length=200, blank=True, null=True)
	name = models.CharField(max_length=200,blank=True, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	building = models.CharField(max_length=200, blank=True, null=True) #building cost+design+documentation and approval
	total_project_price = models.CharField(max_length=200, blank=True, null=True) #project price+building price
	temp =  models.CharField(max_length=200, blank=True, null=True)
	temp_cost = models.CharField(max_length=200, blank=True, null=True)
	apts = models.CharField(max_length=200, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


	
	def __str__(self):
		return self.location


class Liquidity(models.Model):

	STATUS = (
		('Starting', 'Starting'),
		('Filling_up', 'Filling_up'),
		('Completed', 'Completed'),
		)
	topic = models.CharField(max_length=200, blank=True, null=True)
	name = models.CharField(max_length=200,  blank=True, null=True)
	price = models.CharField(max_length=200,  blank=True, null=True)
	status = models.CharField(max_length=200,  null=True, choices=STATUS)
	smart_contracts = models.TextField( blank=True, null=True)
	
	def __str__(self):
		return self.name

class Building(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	fbm6 = models. ImageField(blank=True, null=True,upload_to='images/')
	
	def __str__(self):
		return self.name	

class Plan(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name	

class Token(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name	

class Guest(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name	

class Information1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name	

class Information2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name
	
class Hostingrules(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Vaccineprotocol1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Vaccineprotocol2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Rentreduction(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name	

class Tokenprogram1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Tokenprogram2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Rentopportunity(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Ourcommunity1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Ourcommunity2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Development1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Overview1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Overview2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Guestrules(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Costtrasparency(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Guestopportunity(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Reservation(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Payment1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Payment2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Trading(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Investorsrules(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Tradingclarity(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Tokenprogram3(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Tradingdesk(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Ourcommunity3(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Report(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class News(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Collateral(models.Model):

	state = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	ministry = models.CharField(max_length=200, blank=True, null=True)
	pool = models.CharField(max_length=200, blank=True, null=True)
	amount = models.CharField(max_length=200, blank=True, null=True)
	


	def __str__(self):
		return self.state


class Gov(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Fbm(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Owner(models.Model):
	location = models.CharField(max_length=200, blank=True, null=True)
	agreement_govern = models.CharField(max_length=200, null=True)
	agreement_investor = models.CharField(max_length=200, null=True)
	agreement_property_owner = models.CharField(max_length=200, null=True)
	agreement_tenant = models.CharField(max_length=200, null=True)
	agreement_guest = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.location

class Gin(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Pro(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Ten(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Sub(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Impressum(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Vigna(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name

class Stand(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Apts(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name



class Commit(models.Model):
	location = models.CharField(max_length=200, blank=True, null=True)
	agreement_govern = models.CharField(max_length=200, null=True)
	agreement_investor = models.CharField(max_length=200, null=True)
	agreement_property_owner = models.CharField(max_length=200, null=True)
	agreement_tenant = models.CharField(max_length=200, null=True)
	agreement_guest = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.location



class Design1(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Design2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Design3(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Design4(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name


class Design5(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	
	
	def __str__(self):
		return self.name