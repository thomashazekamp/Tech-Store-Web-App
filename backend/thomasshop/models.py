from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class APIUser(AbstractUser):
    pass

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=200, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    image = models.FileField(upload_to='products', null=True)

class Basket(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

class BasketItem(models.Model):
    id = models.IntegerField(primary_key=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def item_price(self):
        return self.product_id.price * self.quantity
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    datetime_ordered = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    email = models.EmailField()
    delivery_instructions = models.TextField(max_length=250, null=True)
    shipping_addr = models.TextField(default="")
    billing_addr = models.TextField(default="")
