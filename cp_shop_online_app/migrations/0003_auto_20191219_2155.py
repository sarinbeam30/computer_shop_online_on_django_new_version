# Generated by Django 2.2.7 on 2019-12-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_shop_online_app', '0002_all_notebook_product_page_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_notebook_product_page',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
