from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# HTTP REQUEST
def home(request):
    # return HTTP Response
    return render(request, 'recipes/pages/home.html')


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return HttpResponse('CONTATO')

