from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Women, Women2, Women5, Women4, Women6


def material(request):
    product = Women.objects.all().first()
    return render(request, 'women/material.html', {'article': product})


def index(request):
    product = Women4.objects.all().first()
    return render(request, 'women/index.html', {'article': product})


def after(request):
    product = Women2.objects.all().first()
    return render(request, 'women/after.html', {'article': product})


def mn(request):
    product = Women5.objects.all().first()
    return render(request, 'women/mn.html', {'article': product})


def olympics(request):
    product = Women6.objects.all().first()
    return render(request, 'women/olympics.html', {'article': product})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Cтраница не найдена</h1>")


