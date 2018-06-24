"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import re_path, path

from . import views

urlpatterns = [
	re_path('^$', views.index, name='index'),
	re_path('^login/$', views.login, name='login'),
	re_path('^register/$', views.register, name='register'),
	re_path('^profile/$', views.login, name='login'),
	re_path('^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
	re_path('books/$', views.books, name='books'),
	re_path('books/(?P<book_id>[0-9]+)/$', views.details, name='details'),

]
