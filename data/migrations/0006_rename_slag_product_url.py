# Generated by Django 3.2.8 on 2022-06-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_product_slag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slag',
            new_name='url',
        ),
    ]
