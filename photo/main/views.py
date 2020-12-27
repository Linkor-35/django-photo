from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def servises(request):
    return render(request, 'main/index.html')


def goods(request):
    return render(request, 'main/goods.html')


def reklamma(request):
    return render(request, 'main/reklamma.html')


def souvenirs(request):
    return render(request, 'main/souvenirs.html')


def workshop(request):
    return render(request, 'main/workshop.html')


def contacts(request):
    return render(request, 'main/contacts.html')