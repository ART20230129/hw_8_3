import csv
from django.shortcuts import render, redirect
from django.utils.text import slugify

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    if sort == 'name':
        phone_element = Phone.objects.order_by('name')
    elif sort == "min_price":
        phone_element = Phone.objects.order_by('price')
    elif sort == "max_price":
        # phone_element = Phone.objects.order_by('-price')
        phone_element = Phone.objects.order_by('price').reverse()
    else:
        phone_element = Phone.objects.all()

    context = {
        'phones': phone_element,
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {
        'phone': phone,
    }
    return render(request, template, context)
