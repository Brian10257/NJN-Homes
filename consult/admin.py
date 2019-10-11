from django.contrib import admin
from .models import Consult

class ConsultAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'contact_date')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email', 'contact_date')
    list_filter = ('name', 'email', 'contact_date')
    list_per_page = 50
admin.site.register(Consult, ConsultAdmin)