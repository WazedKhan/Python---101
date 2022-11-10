from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello Web World from Django')

def goodbye(request):
    return HttpResponse('Goodbye Web World from Django')

def tawsif(request):
    return HttpResponse('Hello Twasif')