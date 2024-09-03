from django.shortcuts import render


# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'catalog/app_name/index.html')


def contacts(request, *args, **kwargs):
    return render(request, 'catalog/app_name/contacts.html')
