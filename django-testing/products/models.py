from xml.dom import ValidationErr

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

class User(AbstractUser):
    pass

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock_count=models.IntegerField(default=0)

    class Meta:
        constraints=[
            models.CheckConstraint(
                condition=models.Q(price__gt=0),name='price_greater_than_0'
            ),
            models.CheckConstraint(
                condition=models.Q(stock_count__gt=0),name='stock_greater_than_0'
            )
        ]

    def get_discounted_price(self,percent_dis):
        return self.price*(1-percent_dis/100)

    @property
    def in_stock(self) -> bool:
        return self.stock_count > 0

    def clean(self):
        if self.price<0:
            raise  ValidationError("price can't be negative")
        if self.stock_count<0:
            raise ValidationError("Stock can't be negative") 

