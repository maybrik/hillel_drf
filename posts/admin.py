from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'image']
    search_fields = ['title', 'author']
    ordering = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'text', 'for_post']
    search_fields = ['author']
    ordering = ['author']
