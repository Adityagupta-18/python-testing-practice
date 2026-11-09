from .views import home, products, login, profile, api_data, products
from django.urls import path


urlpatterns = [
    path('',home,name='home-page'),
    path('products/',products,name='products'),
    path('login/',login, name='login'),
    path('profile/',profile, name='profile'),
    path('api/',api_data, name='api_data'),

    # DRF END points:
    path('api/products/',products,name='products-api')
]