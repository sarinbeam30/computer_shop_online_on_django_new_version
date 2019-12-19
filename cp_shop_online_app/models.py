from django.db import models
from django.utils import timezone

class All_notebook_product_page(models.Model):
    product_image = models.ImageField(upload_to='Image/all_product/',default= 'default.png', blank=True, max_length=500)
    brand = models.CharField(max_length=30)
    product_detail = models.CharField(max_length=200)
    display = models.CharField(max_length=100)
    graphics = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    processor = models.CharField(max_length=200)
    storage = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)

    special_price = models.IntegerField(default=0)
    normal_price = models.IntegerField(default=0)
    save_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_detail