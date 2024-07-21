from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields": ["title", "author"]}),
        ("Review", {"fields": ["is_favorite", "review", "review_date"]}),
    ]
    readonly_fields = ("review_date",)
    list_display = ("title", "display_authors", "review_date", "is_favorite")

    def display_authors(self, obj):
        return obj.list_authors()

    display_authors.short_description = "(Author(s))"
    list_editable = ("is_favorite",)
    list_display_links = ("title", "review_date",)
    list_filter = ["is_favorite"]
    search_fields = ("title", "author__name",)

admin.site.register(Author)