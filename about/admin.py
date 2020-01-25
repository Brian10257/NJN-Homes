from django.contrib import admin

from .models import About
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    list_display_links = ('title', )
    search_fields = ('title',)
    list_per_page = 50

admin.site.register(About, AboutAdmin)
 