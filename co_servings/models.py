
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
		('Display area', 'Dispaly area'),
		('Working station', 'Working station'),
		('Office', 'Office'),
		('Noursing room', 'Noursing room'),
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
	proper = models.CharField(max_length=200, null=True)
	unit = models.CharField(max_length=200, null=True)
	project = models.CharField(max_length=200, null=True)
	projcost = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.location

	
	
	
class Venue(models.Model):

	CATEGORY = (
		('Guestroom', 'Guestroom'),
		('Display area', 'Dispaly area'),
		('Working station', 'Working station'),
		('Office', 'Office'),
		('Noursing room', 'Noursing room'),
		('Food corner', 'Food corner'),
		)
	owner = models.CharField(max_length=200, blank=True, null=True)
	property_price = models.CharField(max_length=200, blank=True, null=True)
	location = models.CharField(max_length=200, blank=True, null=True)
	name = models.CharField(max_length=200,blank=True, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	building = models.CharField(max_length=200, blank=True, null=True) #building cost+design+documentation and approval
	total_project_price = models.CharField(max_length=200, blank=True, null=True) #project price+building price
	
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