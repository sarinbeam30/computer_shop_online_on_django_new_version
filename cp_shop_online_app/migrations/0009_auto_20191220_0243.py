# Generated by Django 2.2.7 on 2019-12-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_shop_online_app', '0008_auto_20191220_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_notebook_product_page',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]