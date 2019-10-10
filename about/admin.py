from django.contrib import admin

from .models import About
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'arreter' )
    list_display_links = ('title', 'arreter')
    search_fields = ('title', 'arreter')
    list_per_page = 50

admin.site.register(About, AboutAdmin)
 