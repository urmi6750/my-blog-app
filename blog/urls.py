from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('', views.Login.as_view(), name='Login'),
    path('', views.LogOut.as_view(), name='Logout'),
    path('', views.SignUpDone.as_view(), name='SignupDone'),
    path('', views.Registration.as_view(), name='Register')
]
