from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse, redirect
from django.utils.text import slugify

class All_notebook_product_page(models.Model):
    product_preview_image = models.ImageField(upload_to='Image/all_notebook_product/',default='default.png', blank=False, max_length=500)
    # PICTURE
    pic1 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/', default='default.png', blank=False, max_length=500)
    pic2 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/', default='default.png', blank=True, max_length=500)
    pic3 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/', default='default.png', blank=True, max_length=500)
    pic4 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/', default='default.png', blank=True, max_length=500)


    product_detail = models.CharField(max_length=200, default="")
    slug = models.SlugField(unique=True, null=False)
    product_description = models.TextField(max_length=500)
    brand = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=30, default="")
    processor = models.CharField(max_length=200, default="")
    processor_speed = models.CharField(max_length=200, default="")
    display = models.CharField(max_length=100, default="")
    memory = models.CharField(max_length=400, default="")
    storage = models.CharField(max_length=100, default="")
    graphics = models.CharField(max_length=100, default="")
    camera = models.CharField(max_length=100, default="")
    audio = models.CharField(max_length=100, default="")
    dimension = models.CharField(max_length=100, default="")
    weight = models.CharField(max_length=100, default="")
    warranty = models.CharField(max_length=100, default="")
    operating_system = models.CharField(max_length=100, default="")
    
    special_price = models.IntegerField(default=0, blank=True)
    normal_price = models.IntegerField(default=0)
    save_price = models.IntegerField(default=0)

    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_detail
    
    def save(self, *args, **kwargs):
        self.slug = 'products/' + slugify(self.product_detail) + '/'
        # print("TEST" + self.slug)
        super(All_notebook_product_page, self).save(*args, **kwargs)
    

