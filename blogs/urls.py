from django.urls import path

from . import views

urlpatterns = [  
    path('blogs', views.BlogList.as_view(), name = 'blogs'),
    path('<slug:slug>/', views.blog, name = 'blog'),
    
] 