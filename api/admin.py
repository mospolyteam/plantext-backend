from django.contrib import admin
from .models import User, Review, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'reading_count', 'reviews_count', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'author', 'description')
    readonly_fields = ('rating', 'reviews_count', 'reading_count', 'quotes_count')
    exclude = ('reading', )


admin.site.register(User)
admin.site.register(Review)
admin.site.register(Book, BookAdmin)
