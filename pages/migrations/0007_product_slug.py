# Generated by Django 4.2.1 on 2023-05-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_product_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
