from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
	## First define a context dict object.
	context = {}

	## This is to show how you can update an object with more key:value pairs.
	context.update({
		"title": "iBooks - Home",
		"msg": "This is a Home page.",
	})
	return render(request, 'home/index.html', context)

def contact(request):
	context = {
		"title": "iBooks - Contact",
		"msg": "This is the Contact page",
	}

	return render(request, 'home/contact.html', context)

def about(request):
	context = {
		"title": "iBooks - About",
		"msg": "This is the About page",
	}

	return render(request, 'home/about.html', context)

def login(request):
	context = {
		"title": "iBooks - Login",
		"msg": "This is the Login page",
	}

	return render(request, 'home/login.html', context)
