from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main.html')


def animals(request):
    return render(request, 'animals.html')


def care(request):
    return render(request, 'care.html')


def finder(request):
    return render(request, 'finder.html')

def login(request):
    return render(request, 'profile.html')