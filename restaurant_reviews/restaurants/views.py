from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_msg = { 'boldmessage': 'this is god damn testing'}
	return render(request, 'restaurants/index.html', context = context_msg)