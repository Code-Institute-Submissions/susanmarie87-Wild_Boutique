"""Url to connect contact view"""
from django.contrib import admin
from django.urls import path
#from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),

]
