from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def products(request):

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            products=Product.objects.all()
            context={'products':products,'form':form}
            return render(request,'products.html',context)

    products=Product.objects.all()
    context={'products':products,'form':ProductForm}
    return render(request,'products.html',context)