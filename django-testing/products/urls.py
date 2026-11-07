from .views import home, products
from django.urls import path


urlpatterns = [
    path('',home,name='home-page'),
    path('products/',products,name='products')
]