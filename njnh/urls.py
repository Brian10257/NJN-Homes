from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('properties.urls')),
    path('', include('blogs.urls')),
    path('', include('contacts.urls')),
    path('', include('agents.urls')),
    path('', include('about.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
