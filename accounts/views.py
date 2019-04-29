from django.shortcuts import render, HttpResponse

def home(request):
    # L'ajout du dossier accounts/ permet d'eviter la confusion avec 
    # le nom de la page, qui pourrait exister deux fois. Django prendrai le premier
    # qu'il voit 
    return render(request, 'accounts/login.html')