from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', LoginView.as_view(template_name='index.html'), name="index"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login")
]
