from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields": ["title", "author"]}),
        ("Review", {"fields": ["is_favorite", "review", "review_date"]}),
    ]
    readonly_fields = ("review_date",)
    list_display = ("title", "display_authors", "review_date", "is_favorite")

    def display_authors(self, obj):
        return obj.list_authors()

    display_authors.short_description = "Book Authors"

admin.site.register(Book, BookAdmin)
admin.site.register(Author)