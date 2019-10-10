from django.urls import path

from . import views

urlpatterns = [
    path('agent#<int:agent_id>', views.agent, name= 'agent'),
    path('agents', views.agents, name = 'agents'),
]  