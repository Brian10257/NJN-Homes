from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
    path('listings/', include('properties.urls')), 
    path('listings/', include('contacts.urls')),
    path('contact/', include('consult.urls')),
    path('account/', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('carriers/', include('carriers.urls')),
    path('blogs/', include('blogs.urls')),
    path('agents/', include('agents.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 