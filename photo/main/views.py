from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


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
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        print(upload_file.name, upload_file.size)
    return render(request, 'main/upload.html')