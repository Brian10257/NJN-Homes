from django.urls import path

from . import views

urlpatterns = [
    path('carriers', views.carriers, name = 'carriers'),
    path('<slug:slug>/', views.carrier, name = 'carrier'),
    path('jobs', views.jobs, name = 'jobs'),
    path('search2', views.search2, name='search2'),
]  