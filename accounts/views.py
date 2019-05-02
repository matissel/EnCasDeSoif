from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User

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

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Sauvegarde dans la base
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form' : form}
        return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    # Récupère l'utilisateur et le renvoie à la vue
    args = {'user' : request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save() 
			return redirect('/account/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form' : form}
		return render(request, 'accounts/edit_profile.html', args)
