# views.py
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        Product.objects.create(name=name, price=price, quantity=quantity, description=description)
        return HttpResponse("Record created successfully :)")
    return render(request, 'create.html')

def read(request):
    products = Product.objects.all()
    return render(request, 'read.html', {'products': products})

def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.description = request.POST.get('description')
        product.save()
        return HttpResponse("Record updated successfully :)")
    return render(request, 'update.html', {'product': product})

def delete(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        product = get_object_or_404(Product, name=name)
        product.delete()
        return HttpResponse("Record deleted successfully :)")
    return render(request, 'delete.html')
