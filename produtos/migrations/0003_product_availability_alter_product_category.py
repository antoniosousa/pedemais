# Generated by Django 5.1.1 on 2024-09-05 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_alter_category_name'),
        ('produtos', '0002_rename_produtos_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.category', unique=True),
        ),
    ]
