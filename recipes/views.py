from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# HTTP REQUEST
def home(request):
    # return HTTP Response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Recipe',
    })


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return HttpResponse('CONTATO')

