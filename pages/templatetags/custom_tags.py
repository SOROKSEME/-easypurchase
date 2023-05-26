from django import template
from pages.models import Category, NewProduct, Product

register = template.Library()


@register.simple_tag()
def get_category():
    categories = Category.objects.all()
    return categories


@register.simple_tag()
def get_new_product():
    new_product = NewProduct.objects.all()
    return new_product


@register.simple_tag()
def get_product():
    product = Product.objects.all()
    return product

