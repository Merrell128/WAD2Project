from django import forms
from restaurants.models import Restaurant, Review, UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator

class RestaurantForm(forms.ModelForm):
	restaurant_name = forms.CharField(max_length=3,
	help_text="Please enter the name of the restaurant.")
	address = forms.CharField(max_length=100,
	help_text="Please enter the address of the restaurant")
	telepohne = forms.IntegerField(help_text="Please enter the phone number of the restaurant if there is one")
	
	
	class Meta:
		model = Restaurant
		fields = ('restaurant_name', 'picture','cuisine', 'address', 'telephone')

class ReviewForm(forms.ModelForm):
	rating = forms.IntegerField(help_text = 'Enter a value from 1 to 5')
	review = forms.CharField(required = False)
	
	class Meta:
		model = Review
		
		fields = '__all__'
		
		
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = UserProfile
		
		fields = ('user', 'password', 'name')
		
class UserProfileForm(forms.ModelForm):
	owner = forms.BooleanField(help_text = 'Check if you are an owner of a restaurant')
	
	class Meta:
		model = UserProfile
		
		fields = ('owner',)
