from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.agent, name= 'agent'),
    path('agents', views.agents, name = 'agents'),
]  