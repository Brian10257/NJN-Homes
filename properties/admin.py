from django.contrib import admin

from .models import Property_single

class Property_singleAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'is_published', 'price', 'list_date')
    list_display_links = ('title', 'city', 'price')
    list_filter = ('title', 'city' ) 
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'state', 'zipcode')
    list_per_page = 20
    prepopulated_fields = {'slug': ('state', 'title')}
admin.site.register(Property_single, Property_singleAdmin)