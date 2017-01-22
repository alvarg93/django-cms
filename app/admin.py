from django.contrib import admin

from .models import Book, Boot, Post


# Register your models here.


def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


duplicate.short_description = "Duplicate selected record"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "stock", "year")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    ordering = ['-created_at']
    actions = [duplicate]


admin.site.register(Book, BookAdmin)
admin.site.register(Boot)
admin.site.register(Post, PostAdmin)
