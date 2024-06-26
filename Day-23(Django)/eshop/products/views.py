from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# def index(request):
#     return HttpResponse("Welcome to Products page")

def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products":products})

def new(request):
    return render(request,"new.html")