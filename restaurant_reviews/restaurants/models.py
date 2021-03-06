from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=30)
	address = models.CharField(max_length=100, unique=True)
	telephone = models.IntegerField()
	cuisine = models.CharField(max_length=30)
	picture = models.FileField(upload_to='restaurants_uploads/')
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'restaurants'

	def __str__(self):
		return self.name
	


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField
	picture = models.FileField(upload_to='profile_images', blank=True)
	owner = models.BooleanField(default=False)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=30)

	def __str__(self):
		return self.user.username
        
class Review(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)	
	username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now, blank=True)
	rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
	review = models.CharField(max_length=300)
	

	def __str__(self):
		return self.question_text