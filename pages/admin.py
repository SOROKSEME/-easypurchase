from django.contrib import admin
from .models import Category, NewProduct, Product

# Регистрируйте своих моделей здесь.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewProduct)
class NewProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "publisher", "developer", "category")
    list_display_links = ("pk", "title")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("title",)}
