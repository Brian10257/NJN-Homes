from django.contrib import admin

from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'link')
    list_display_links = ('title', 'upload_date')
    list_filter = ('title', 'upload_date', 'link' ) 
    search_fields = ('title', 'upload_date', 'link')
    list_per_page = 20
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Service, ServiceAdmin) 