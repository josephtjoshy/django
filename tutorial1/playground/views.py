from django.shortcuts import render
from django.http import HttpResponse

def say_hellow(request):
    return HttpResponse('Hellow world')
