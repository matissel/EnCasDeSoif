from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from accounts.forms import EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pointsEau.models import PointEau
from django.contrib.auth import login, authenticate
from django.core import serializers
from django.contrib import messages as msg
from EnCasDeSoif.views import index


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Sauvegarde dans la base
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg.success(request, "Vous venez de créer un compte ! Bienvenue")
            return redirect('/')
    else:
        form = UserCreationForm()

    args = {'form': form, 'active': 'register'}
    return render(request, 'accounts/reg_form.html', args)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            msg.info(request, "Vous êtes maintenant connecté !")
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'active': 'login'})


@login_required
def view_profile(request):
    # Récupère l'utilisateur et le renvoie à la vue
    args = {'user': request.user,
            'active': 'profile'}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg.success(request, "Votre profil a bien été modifié")
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form,
                'active': 'profile'}
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
        'form': form,
        'active': 'profile'
    })


@login_required
def view_logout(request):
    logout(request)
    msg.info(request, "A bientôt l'ami !")
    return index(request)
