from django.contrib import admin

from .models import News, Category

"""Отображение в админке"""
class NewsAdmin(admin.ModelAdmin):
    """Отображение полей"""
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    """Конкретные поля становятся ссылками"""
    list_display_links = ('id', 'title')
    """Поиск по полям"""
    search_fields = ('title', 'content')
    """Поле, которое мы можем редактировать прямо из админки"""
    list_editable = ('is_published',)
    """По каким полям фильтруем"""
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



