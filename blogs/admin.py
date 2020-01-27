from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'date_published')
    list_filter = ('status', 'title', 'date_published')
    search_fields = ('title', 'sub_title', 'status', 'category', 'content')
    list_display_links = ('title', 'category')
    list_per_page = 30
    prepopulated_fields = {'slug': ('title', 'sub_title', 'category')}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'comment_date', 'active')
    list_display_links = ['name', 'post']
    list_filter = ('active', 'comment_date')
    list_per_page = 90
    list_editable = ('active',)
    search_fields = ('name', 'email', 'body', 'website')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Blog, BlogAdmin)
