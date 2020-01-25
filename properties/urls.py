from django.urls import path

from . import views

urlpatterns = [
    path('properties', views.properties, name = 'properties'),
    path('<slug:slug>/', views.property_single, name= 'property_single'),
    path('search', views.search, name='search'), 
]   