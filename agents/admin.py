from django.contrib import admin

from .models import Agent
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role','email' ,'phone', 'hire_date' )
    list_display_links = ('name','role', 'email')
    search_fields = ('name','role', 'hire_date')
    list_per_page = 50

admin.site.register(Agent, AgentAdmin)
 