from django.contrib import admin

from .models import About
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'name' )
    list_display_links = ('title', 'name')
    search_fields = ('title', 'name')
    list_per_page = 50

admin.site.register(About, AboutAdmin)
 