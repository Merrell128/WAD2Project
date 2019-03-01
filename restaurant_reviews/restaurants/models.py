from django.db import models
from datetime import datetime 

class User(models.Model):
	fullname = models.CharField(max_length=50)
	username = models.CharField(max_length=30, unique=True)
	email = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=16)
	picture = models.FileField(upload_to='uploads/')
	owner = models.BooleanField(default=False)
	
class Restaurant(models.Model):
	idNumber = models.IntegerField(max_length=5, unique=True)
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	telephone = models.IntegerField(max_length=14)
	Cuisine = models.CharField(max_length=30)
	picture = models.FileField(upload_to='restaurants_uploads/')
	
class Review(models.Model):
	idReview = (('Restaurant.idNumber', 'User.username'))	
	username = User.username
	date = models.DateTimeField(default=datetime.now, blank=True)
	rating = models.IntegerField(max_length=1)
	review = models.CharField(max_length=300)