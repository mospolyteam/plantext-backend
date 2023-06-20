from django.contrib import admin
from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse

from .models import User, Review, Book, Quote, BookRatingRelationship, Article, WriterRatingRelationship, Writer, \
    Partner, Visit


def create_link(text, url, target=False):
    return f'<a href="{url}" target="{"_blank" if target else "_self"}">{text}</a>'


class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'url', 'method')
    search_fields = ('user',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'reading_count', 'reviews_count', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'author', 'description')
    readonly_fields = ('rating', 'reviews_count', 'reading_count', 'quotes_count')
    exclude = ('reading',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'excerpt', 'user', 'get_book', 'created_at', 'is_published')
    list_display_links = ('id',)
    search_fields = ('id', 'text_review')
    list_editable = ('is_published',)
    list_filter = ('created_at', 'is_published')
    autocomplete_fields = ('book', 'user')
    readonly_fields = ('created_at',)

    def excerpt(self, obj):
        url = reverse('admin:api_review_change', args=(obj.id,))
        link = create_link(obj.text_review[:16], url)
        return mark_safe(link)

    excerpt.short_description = 'Содержание'

    def get_book(self, obj):
        url = reverse('admin:api_book_change', args=(obj.id,))
        link = create_link('(просмотреть)', url, True)
        return mark_safe(f'<span>{obj.book} {link}</span>')

    get_book.short_description = 'Книга'


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_book', 'excerpt', 'author', 'created_at', 'is_published')
    list_display_links = ('id',)
    list_filter = ('created_at', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('text',)
    readonly_fields = ('created_at',)
    autocomplete_fields = ('book', 'author')

    def excerpt(self, obj):
        url = reverse('admin:api_quote_change', args=(obj.id,))
        link = create_link(obj.text[:16], url)
        return mark_safe(link)

    excerpt.short_description = 'Текст'

    def get_book(self, obj):
        url = reverse('admin:api_book_change', args=(obj.id,))
        link = create_link('(просмотреть)', url, True)
        return mark_safe(f'<span>{obj.book} {link}</span>')

    get_book.short_description = 'Книга'


class BookRatingRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'value', 'created_at')
    list_display_links = ('id', 'value', 'book', 'user')
    list_filter = ('value', 'created_at')
    readonly_fields = ('created_at',)
    autocomplete_fields = ('book', 'user')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('created_at',)
    search_fields = ('title', 'text')
    readonly_fields = ('created_at',)
    autocomplete_fields = ('author',)


class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'death_day')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('birthday', 'death_day')


class WriterRatingRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'user', 'value', 'created_at')
    list_display_links = ('id', 'writer', 'user', 'value')
    list_filter = ('created_at', 'value')
    readonly_fields = ('created_at',)
    autocomplete_fields = ('writer', 'user')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image', 'get_link')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'link')

    def get_image(self, obj):
        if obj.image:
            url = reverse('admin:api_partner_change', args=(obj.id,))
            img = f'<img height="150px" src="/media/{obj.image}" />'
            link = create_link(img, url)
            return mark_safe(link)
        return 'Изображение отсутствует..'

    get_image.short_description = 'Изображение'

    def get_link(self, obj):
        if obj.link:
            link = create_link('Перейти на сайт партнера', obj.link, True)
            return mark_safe(link)
        return 'Ссылка на партнера отсутствует..'

    get_link.short_description = 'Сайт партнера'


admin.site.register(Visit, VisitAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(BookRatingRelationship, BookRatingRelationshipAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(WriterRatingRelationship, WriterRatingRelationshipAdmin)
admin.site.register(Partner, PartnerAdmin)
