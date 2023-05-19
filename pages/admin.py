from django.contrib import admin
from .models import Category

# Регистрируйте своих моделей здесь.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}
