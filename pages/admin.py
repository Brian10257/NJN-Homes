from django.contrib import admin

from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('manager_name', 'phone', 'is_published')
    list_display_links = ('manager_name', 'phone')
    list_filter = ('manager_name', 'phone' )
    list_editable = ('is_published',)
    search_fields = ('manager_name', 'phone')
    list_per_page = 20
admin.site.register(Services, ServicesAdmin)