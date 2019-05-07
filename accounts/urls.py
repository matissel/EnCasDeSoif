from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView, LogoutView, PasswordResetView, PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', views.view_logout, name='logout'),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),

]
