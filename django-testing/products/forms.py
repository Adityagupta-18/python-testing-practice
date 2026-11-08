from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ("name","price", "stock_count")

    def clean_price(self):
        price=self.cleaned_data.get("price")
        if price<0:
            raise ValidationError("price can't be negative")
        return price

    def clean_stock_Count(self):
        stock=self.cleaned_data.get('stock_count')
        if stock<0:
            raise ValidationError("stock can't be negative")
        return stock