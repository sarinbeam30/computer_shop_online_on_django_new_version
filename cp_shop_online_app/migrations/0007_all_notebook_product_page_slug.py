# Generated by Django 2.2.7 on 2019-12-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_shop_online_app', '0006_auto_20191219_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_notebook_product_page',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
