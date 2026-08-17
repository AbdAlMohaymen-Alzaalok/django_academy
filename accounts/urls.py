from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import forms,views

urlpatterns = [
path('',include('django.contrib.auth.urls')),
path('login/',LoginView.as_view(authentication_form=forms.LoginForm),name='login'),
path('register/',views.CreateUser.as_view(),name='register'),
path('profile/',views.edit_form,name='profile'),
]
