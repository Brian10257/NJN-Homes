from django.urls import path

from . import views
from properties.views import *
 
urlpatterns = [
    path('contacts', views.contact, name='contact'),
    
]
 