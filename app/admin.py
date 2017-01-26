from django.contrib import admin

from .models import Post, Author, Comment, duplicate, publish, unpublish

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published", "author")
    ordering = ['-created_at']
    actions = [duplicate, publish, unpublish]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    ordering = ['-created_at']
    actions = [duplicate]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "created_at", "author")
    ordering = ['-created_at']
    actions = [duplicate]

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
