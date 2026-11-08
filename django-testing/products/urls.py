from .views import home, products, login, profile
from django.urls import path


urlpatterns = [
    path('',home,name='home-page'),
    path('products/',products,name='products'),
    path('login/',login, name='login'),
    path('profile/',profile, name='profile'),
]