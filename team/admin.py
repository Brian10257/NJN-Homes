from django.contrib import admin

from .models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'date_posted', 'facebook')
    list_display_links = ('name', 'role')
    list_filter = ('name', 'role', 'date_posted')
    search_fields = ('name', 'role')
    list_per_page = (50)
admin.site.register(Team, TeamAdmin)