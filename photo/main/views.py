from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def servises(request):
    return render(request, 'main/index.html')


def goods(request):
    return render(request, 'main/index.html')


def reklamma(request):
    return render(request, 'main/index.html')


def souvenirs(request):
    return render(request, 'main/index.html')


def workshop(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/index.html')