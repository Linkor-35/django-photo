from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import OrderForm, PhotoForm


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


def upload(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        # тут нужно внести данные в поле "order_uidd"
        if form.is_valid():
            form.save()
            return render(request, 'main/upload_done.html')

    if request.method == "GET":
        form = OrderForm()
        photo = PhotoForm()

        return render(request, 'main/upload.html', {
            'form' : form,
            'photo' : photo
        })


def upload_done(request):
    return render(request, 'main/upload_done.html')

