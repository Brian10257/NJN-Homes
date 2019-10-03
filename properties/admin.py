from django.contrib import admin

from .models import Property_single

class Property_singleAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'is_published', 'price', 'list_date', 'agent')
    list_display_links = ('city', 'title')
    list_filter = ('agent', 'city' )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 20
admin.site.register(Property_single, Property_singleAdmin)