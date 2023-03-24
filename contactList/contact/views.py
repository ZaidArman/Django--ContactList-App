from django.shortcuts import render
from django.http import HttpResponse
from . models import ContactlistModel

# Create your views here.

def hello(request):
    return HttpResponse('Hello, World!')

def display(request):
    contacts = ContactlistModel.objects.all()
    S = " "
    for c in contacts:
        S += c.to_string() + '<br>'
    return HttpResponse('Contacts: <br>' + S)
    
    