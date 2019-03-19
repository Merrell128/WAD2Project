from restaurants.models import Restaurant, Review
from restaurants.forms import UserForm, UserProfileForm, RestaurantForm, ReviewForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
	restaurant_list = Restaurant.objects.order_by('-likes')[:5]
	context_msg = {'restaurants': restaurant_list}
	return render(request, 'restaurants/index.html', context = context_msg)

def show_restaurant(request, category_name_slug):
	context_dict = {}

	try:
		restaurant = Restaurant.objects.get(slug=category_name_slug)
		reviews = Reviews.objects.filter(category=category)
		context_dict['reviews'] = reviews
		context_dict['restaurants'] = restaurant

	except Restaurant.DoesNotExist:
		context_dict['restaurants'] = None
		context_dict['reviews'] = None

	return render(request, 'restaurants/restaurant.html', context_dict)

def add_restaurant(request):
	form = RestaurantForm()

	if request.method == 'POST':
		form = RestaurantForm(request.POST)
	 
	return render(request, 'restaurants/add_restaurant.html', {})
	
def add_review(request, category_name_slug):
    try:
        restaurant = Restaurant.objects.get(slug=category_name_slug)
    except Restaurant.DoesNotExist:
        restaurant = None

    form = PageForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if restaurant:
                review = form.save(commit=False)
                review.category = category
                review.views = 0
                review.save()
                return show_restaurant(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'restaurant': restaurant}
    return render(request, 'restaurants/add_review.html', context_dict)    


def about(request):
	return render(request,'restaurants/about.html')

def register(request):
	registered = False;

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
				  'restaurants/register.html',
				  {'user_form': user_form,
				   'profile_form': profile_form,
				   'registered': registered})

	if form.is_valid():
		form.save(commit=True)
		return index(request)
	else:
		print(form.errors)

	return render(request, 'restaurants/add_restaurant.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'restaurants/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


