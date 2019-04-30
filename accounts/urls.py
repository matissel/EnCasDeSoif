from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login")
]
