from django.contrib import admin

from .models import Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'category', 'date_published' )
    list_display_links = ('title', 'author_name')
    search_fields = ('title', 'author_name', 'category')
    list_per_page = 50

admin.site.register(Blog, BlogAdmin)
 