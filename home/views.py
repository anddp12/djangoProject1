from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>HOME</h1>")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("<h1>ABOUT</h1>")
    return render(request, 'about.html')
