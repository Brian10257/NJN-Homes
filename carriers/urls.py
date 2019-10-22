from django.urls import path

from . import views

urlpatterns = [
    path('carriers', views.carriers, name = 'carriers'),
    path('carrier#<int:carrier_id>', views.carrier, name = 'carrier'),
    path('jobs', views.jobs, name = 'jobs'),
    path('search2', views.search2, name='search2'),
]  