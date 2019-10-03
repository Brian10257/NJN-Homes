from django.urls import path

from . import views

urlpatterns = [
    path('agents', views.agents, name = 'agents'),
    path('<int:agent_id>', views.agent, name= 'agent'),
]  