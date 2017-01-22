from django.contrib import admin

from .models import Post, duplicate, publish, unpublish

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "is_published")
    ordering = ['-created_at']
    actions = [duplicate, publish, unpublish]

admin.site.register(Post, PostAdmin)
