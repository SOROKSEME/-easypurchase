from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.


class NewProduct(models.Model):
    image = models.ImageField(verbose_name="Фото", blank=True, null=True)
    title = models.CharField(verbose_name="Название нового продукта", max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Название нового продукта"
        verbose_name_plural = "Название новыйх продуктов"


class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def get_absolute_url(self):
        return reverse("category_products", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    image = models.ImageField(verbose_name="Фото", blank=True, null=True)
    title = models.CharField(verbose_name="Название игры", max_length=150)
    price = models.CharField(verbose_name="Цена", max_length=150)
    description = models.TextField(verbose_name="Описание игры", max_length=200)
    publisher = models.CharField(verbose_name="Издатель", max_length=150, null=True)
    data = models.DateField(verbose_name="Дата выхода", auto_now_add=False, null=True)
    developer = models.CharField(verbose_name="Разработчик", max_length=150, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def add_to_cart(self):
        return reverse("to_cart", kwargs={"product_id": self.pk, "action": "add"})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продук"
        verbose_name_plural = "Продукты"
