from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),


    path('Login/', views.Login.as_view(), name='Login'),
    path('Logout/', views.LogOut.as_view(), name='Logout'),
    path('Profile/',  views.Profile.as_view(), name='Profile'),
    path('Register/', views.Registration.as_view(), name='Register'),
    path('SignUpDone/', views.SignUpDone.as_view(), name='SignUpDone'),
]
