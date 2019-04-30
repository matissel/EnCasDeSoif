from django.shortcuts import render, HttpResponse

def home(request):
    # L'ajout du dossier accounts/ permet d'eviter la confusion avec 
    # le nom de la page, qui pourrait exister deux fois. Django prendrai le premier
    # qu'il voit 
    numbers = [1,2,3,4,5]
    name = "Matisse"
    args = {'name':name,'numbers':numbers}
    return render(request, 'home.html', args)

def index(request):
    return render(request, 'index.html')