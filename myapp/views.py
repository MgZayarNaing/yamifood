from django.shortcuts import render
from .models import *
# Create your views here.

def home_list(request):
    imageslider = Imageslider.objects.all().order_by('-id')
    startabout = Startabout.objects.all().order_by('id')[:1]
    gallery = Gallery.objects.all().order_by('-id')[:6]
    customerReviews = CustomerReviews.objects.all().order_by('-id')[:6]
    information = Information.objects.all()[:1]

    return render(request, 'index.html', {'imageslider': imageslider,'startabout':startabout,'gallery':gallery,'customerReviews':customerReviews,'information':information})

def menu_list(request):
    categories = Categories.objects.all().order_by('-id')

    return render(request,'menu.html', {'categories':categories})