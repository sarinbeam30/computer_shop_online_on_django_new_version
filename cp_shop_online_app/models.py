from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from django.shortcuts import  redirect , reverse
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect


class All_notebook_product_page(models.Model):
    product_preview_image = models.ImageField(
        upload_to='Image/all_notebook_product/', default='default.png', blank=False, max_length=500)
    # PICTURE
    pic1 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/',
                             default='default.png', blank=False, max_length=500)
    pic2 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/',
                             default='default.png', blank=True, max_length=500)
    pic3 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/',
                             default='default.png', blank=True, max_length=500)
    pic4 = models.ImageField(upload_to='Image/all_notebook_product/full_resol_image/',
                             default='default.png', blank=True, max_length=500)

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
    quantity = models.IntegerField(default=1)
    special_price = models.IntegerField(default=0)
    normal_price = models.IntegerField(default=0)
    save_price = models.IntegerField(default=0)

    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_detail

    def save(self, *args, **kwargs):
        self.slug = 'products/' + slugify(self.product_detail) + '/'
        # print("TEST" + self.slug)
        super(All_notebook_product_page, self).save(*args, **kwargs)

    def get_absolute_url(self , slug):
        return reverse("product_detail_page", kwargs={
            'slug': slug
        })

    def get_add_to_cart_url(self , slug):
        return reverse("cp_shop_online_app:add-to-cart", kwargs={
            'slug': slug
        })

    # def get_add_to_cart_url(self):
    #     return redirect("cp_shop_online_app:main_page", slug=self.slug)

    # def get_remove_from_cart_url(self):
    #     return reverse("cp_shop_online_app:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(All_notebook_product_page,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.brand}"

    # def get_total_item_price(self):
    #     return self.quantity * self.item.price

    # def get_total_discount_item_price(self):
    #     return self.quantity * self.item.special_price

    # def get_amount_saved(self):
    #     return self.get_total_item_price() - self.get_total_discount_item_price()

    # def get_final_price(self):
    #     if self.item.special_price:
    #         return self.get_total_discount_item_price()
    #     return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    # def get_total(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         total += order_item.get_final_price()
    #     if self.coupon:
    #         total -= self.coupon.amount
    #     return total
