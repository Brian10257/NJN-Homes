from django.contrib import admin
from .models import Carrier, Apply

class CarrierAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'job_available', 'address', 'employer', 'website', 'is_published')
    list_display_links = ( 'company', 'job_title', 'address', 'employer', 'website')
    search_fields = ( 'company', 'job_title', 'address', 'employer', 'website')
    list_filter = ( 'company', 'job_title', 'address', 'employer', 'website')
    list_per_page = 50
    prepopulated_fields = {'slug': ('company', 'job_title')}


class ApplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'current_city', 'application_date')
    list_display_links = ( 'name', 'email', 'application_date',)
    search_fields = ('name', 'email', 'phone', 'place_of_origin', 'current_city', 'current_employment', 'neighbour_hood')
    list_filter = ( 'name', 'email', 'phone', 'place_of_origin', 'current_city', 'current_employment', 'neighbour_hood')
    list_per_page = 50
    model = Apply
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Apply, ApplyAdmin)

