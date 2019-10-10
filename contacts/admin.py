from django.contrib import admin

from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'contact_date' )
    list_display_links = ('name', 'email')
    search_fields = ('name', 'contact_date')
    list_per_page = 50

admin.site.register(Contact, ContactAdmin)
 