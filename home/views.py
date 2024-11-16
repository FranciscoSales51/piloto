from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<p>A view index funcionou, Wow!</p>")
    return render(request, 'home/index.html')


def sobre(request):    
    # return HttpResponse('Sobre o sistema')
    return render(request,'home/sobre.html')

def contato(request):
    return render(request,'home/contato.html')