from products.models import Product
from rest_framework import serializers
from django.core.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    in_stock=serializers.BooleanField(read_only=True)

    class Meta:
        model=Product
        fields='__all__'
        read_only_fields=['id','in_stock']

    def validate_price(self,value):
        if value<0:
            raise ValidationError("Price can't be negative")
        return value

    def validate_stock_count(self,value):
        if value<0:
            raise ValidationError("Stock can't be negative")
        return value