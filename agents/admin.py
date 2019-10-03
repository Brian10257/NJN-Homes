from django.contrib import admin

from .models import Agent
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'hire_date' )
    list_display_links = ('name', 'email')
    search_fields = ('name', 'hire_date')
    list_per_page = 50

admin.site.register(Agent, AgentAdmin)
 