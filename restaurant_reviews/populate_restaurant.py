import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','restaurant_reviews.settings')
import django
django.setup()
from restaurants.models import Restaurant, Review, UserProfile
from django.contrib.auth.models import User
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, 'restaurant_reviews\\media\\')
from django.core.files.images import ImageFile

def populate():
	# Restaurant owners
	restaurant_owners = [{'user': 'charstefanos', 'password': '123a456b789c', 'name': 'Stefanos Owner', 'email' : 'charstefanos@gmail.com', 'owner' : True},
						{'user': 'hughmerrell', 'password': '1abc@#Qas', 'name': 'Hugh Owner', 'email' : 'hughmerrel@gmail.com', 'owner' : True},
						{'user': 'alanmcnamee', 'password': '@un0w3#!', 'name': 'Alan Owner', 'email' : 'alanmcnamee@gmail.com',  'owner' : True},
						{'user': 'asadmahmood', 'password': '@dm1n1dk*', 'name': 'Asad Owner', 'emai' : 'asadmahmood@gmail.com', 'owner' : True}]
						
	customers = [{'user': 'stefanoscha', 'password': '123a456b789c', 'name': 'Stefanos Customer', 'email' : 'stefanoscha@gmail.com', 'owner' : False},
				{'user': 'merrellhugh', 'password': '1abc@#Qas', 'name': 'Hugh Customer', 'email' : 'merrellhugh@gmail.com', 'owner' : False},
				{'user': 'mcnameealan', 'password': '@un0w3#!', 'name': 'Alan Customer', 'email' : 'mcnameealan@gmail.com',  'owner' : False},
				{'user': 'mahmoodasad', 'password': '@dm1n1dk*', 'name': 'Asad Customer', 'email' : 'mahmoodasad@gmail.com', 'owner' : False}]
				
	restaurants = {'charstefanos': [{'restaurant_name' : 'Subway', 'cuisine' : 'Thai', 'address' : '32 University Avenue, Glasgow G12 8LX', 'telephone' : '01413397448'}],
				'hughmerrell': [{'restaurant_name' : 'Amarone', 'cuisine' : 'Italian', 'address': '2 Nelson Mandela Pl, Glasgow G2 1BT', 'telephone' : '01413331122'}],
				'alanmcnamee': [{'restaurant_name' : 'Cote Brasserie', 'cuisine' : 'Modern', 'address': '41-43 W Nile St, Glasgow G1 2PT', 'telephone' : '01412481022'}]}
	
	reviews = {'Subway': [{'customer_username': 'stefanoscha', 'rating' : 3, 'review' : 'Great place with lovely food.'},
						{'customer_username': 'merrellhugh', 'rating' : 5, 'review' : 'Best place I have been. great service.'},
						{'customer_username': 'mahmoodasad', 'rating': 1, 'review' : 'the food was cold and the place was dirty.'}],
				'Amarone':[{'customer_username': 'mcnameealan', 'rating' : 1, 'review' : 'Never heard of it in my life, never been either.'},
						{'customer_username' : 'stefanoscha', 'rating' : 2, 'review' : 'Had better elsewhere.'},
						{'customer_username' : 'merrellhugh', 'rating' :5, 'review' : 'My cousin owns the restaurant so I always eat for free.'}],
				'Cote Brasserie': [{'customer_username': 'merrellhugh', 'rating' : 3, 'review' : 'Great food but got food poisoning afterwards, worth it.'},
								{'customer_username' : 'mcnameealan' , 'rating' : 4, 'review' : 'Not bad, needs improvement.'},
								{'customer_username' : 'mahmoodasad' , 'rating' : 5, 'review' : 'Best pizza in town,MUST TRY!!'}]}
	
	users = {}
	for	customer_info in customers:
		c = add_user(customer_info["user"], customer_info["password"], customer_info["name"], customer_info["email"], customer_info["owner"])
		users[customer_info["user"]] = c
		
	for owner_info in restaurant_owners:
		o = add_user(owner_info["user"], owner_info["password"], owner_info["name"], owner_info["email"], owner_info["owner"])
		for restaurant in restaurants[owner_info["user"]]:
			res = add_restaurant(o, restaurant["restaurant_name"], restaurant["cuisine"], restaurant["address"], restaurant["telephone"])
			for review in reviews[restaurant["restaurant_name"]]:
				rev = add_review(res, users[review["customer_username"]], review["rating"], review["review"])
				
def add_user(user, password, name, email, owner):
	u = User.objects,get_or_create(user = user, password = password, name = name, email = email)[0]
	up = UserProfile.objects.get_or_create(user = u, owner = owner)[0]
	up.save()
	return up
	
def add_restaurant(owner, restaurant_name, cuisine, address, telephone):
	r = Restaurant.objects.get_or_create(owner = owner, restaurant_name = restaurant_name, cuisine = cuisine, address = address, telephone = telephone)[0]
	r.save()
	return r
		
def add_review(restaurant, user, rating, review):
	rev = Review.objects.get_or_create(restaurant = restaurant, user = username, rating = rating, review = review)[0]
	rev.save()
	return rev
		
if __name__ == '__main__':
	print("Starting Restaurant population script...")
	print("Users created:")
	for u in UserProfile.objects.all():
		print(str(u))
		print()
	print("Restaurant created:")
	for res in Restaurant.objects.all():
		print(str(res))
		print("Customers who left a review:")
		for r in Review.objects.filter(restaurant=res):
			print(str(r))
		print()
		populate()
		