from django import forms
from django.forms import ModelForm
from .models import Venue, Liquidity 


class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('owner', 'property_price', 'location', 'name', 'category', 'building', 'total_project_price')

		widgets = {
			'owner': forms.TextInput(attrs={'class':'form-control'}),
			'property_price': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'}),
			
			'location': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'building': forms.TextInput(attrs={'class':'form-control'}),
			'total_project_price': forms.TextInput(attrs={'class':'form-control'}),

		}	
		


class LiquidityForm(ModelForm):
	class Meta:
		model = Liquidity
		fields = ('topic', 'name', 'price', 'status', 'smart_contracts')

		widgets = {
			'topic': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'}),
			
			'smart_contracts': forms.TextInput(attrs={'class':'form-control'}),
			
		}	