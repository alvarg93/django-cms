from django.contrib import admin
from .models import Book, Boot
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "stock", "year")

admin.site.register(Book, BookAdmin)
admin.site.register(Boot)
