from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pointsEau.models import PointEau
from django.core import serializers


def home(request):
    # L'ajout du dossier accounts/ permet d'eviter la confusion avec
    # le nom de la page, qui pourrait exister deux fois. Django prendrai le premier
    # qu'il voit
    numbers = [1, 2, 3, 4, 5]
    name = "Matisse"
    args = {'name': name, 'numbers': numbers}
    return render(request, 'home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Sauvegarde dans la base
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


@login_required
def view_profile(request):
    # Récupère l'utilisateur et le renvoie à la vue
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'accounts/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


@login_required
def view_logout(request):
    logout(request)
    return render(request, 'index.html')
