from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
import requests
from requests.exceptions import RequestException
from django.http import JsonResponse, HttpResponse

from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

def api_data(request):
    try:
        response=requests.get('https://jsonplaceholder.typicode.com/posts/1')
        response.raise_for_status()
        return JsonResponse(response.json())
    except RequestException as e:
        return HttpResponse('error',status=503)



@login_required
def profile(request):
    return render(request,'profile.html')

def login(request):
    return render(request,'login.html')


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




@api_view(['GET', 'POST'])
def products(request):

    if request.method=='GET':
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)