from django.db import models

# Create your models here.
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

	property_price = models.FloatField(null=True)
	location = models.CharField(max_length=200, null=True)
	dimension = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	building = models.CharField(max_length=200, null=True) #building cost+design+documentation and approval
	typology = models.CharField(max_length=200, null=True)
	total_project_price = models.FloatField(null=True) #project price+building price
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.location
	
	

class Liquidity_Pool(models.Model):
	STATUS = (
		('Starting', 'Starting'),
		('Filling-up', 'Filling-up'),
		('Completed', 'Completed'),
		)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.name

	



class Investment(models.Model):
	webinvestor = models.ForeignKey(Webinvestor, null=True, on_delete= models.SET_NULL)
	liquidity_pool = models.ForeignKey(Liquidity_Pool, null=True, on_delete= models.SET_NULL)
	project = models.ForeignKey(Project, null=True, on_delete= models.SET_NULL)
	
	def __str__(self):
		return self.webinvestor.name

