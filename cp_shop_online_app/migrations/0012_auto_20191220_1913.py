# Generated by Django 2.2.7 on 2019-12-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp_shop_online_app', '0011_all_notebook_product_page_processor_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_notebook_product_page',
            name='product_image',
        ),
        migrations.AddField(
            model_name='all_notebook_product_page',
            name='pic1',
            field=models.ImageField(default='default.png', max_length=500, upload_to='Image/all_notebook_product/full_resol_image/'),
        ),
        migrations.AddField(
            model_name='all_notebook_product_page',
            name='pic2',
            field=models.ImageField(blank=True, default='default.png', max_length=500, upload_to='Image/all_notebook_product/full_resol_image/'),
        ),
        migrations.AddField(
            model_name='all_notebook_product_page',
            name='pic3',
            field=models.ImageField(blank=True, default='default.png', max_length=500, upload_to='Image/all_notebook_product/full_resol_image/'),
        ),
        migrations.AddField(
            model_name='all_notebook_product_page',
            name='pic4',
            field=models.ImageField(blank=True, default='default.png', max_length=500, upload_to='Image/all_notebook_product/full_resol_image/'),
        ),
        migrations.AddField(
            model_name='all_notebook_product_page',
            name='product_preview_image',
            field=models.ImageField(default='default.png', max_length=500, upload_to='Image/all_notebook_product/'),
        ),
    ]
