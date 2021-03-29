from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

# Create your views here.

def home(request):
	return render(request,'warehouse/homepage.html')


def products(request):
	all_products = Product.objects.all()
	context = {'all_products':all_products}
	return render(request,'warehouse/products.html', context)

def product_detail(request, product_id):
	product = Product.objects.get(id=product_id)
	#product = get_object_or_404(Product, pk=product_id)
	#product = Propertyobjects.filter('id=product_id')
	context = {'product':product}
	return render(request,'warehouse/product_detail.html', context)



def customer(request):
	return render(request,'warehouse/customer.html')