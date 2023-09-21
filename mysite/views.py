from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request, 'mysite.html')

def about(request):
    return render(request, 'about.html')