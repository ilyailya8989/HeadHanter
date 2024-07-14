from django.urls import path
from user import views

urlpatterns = [
    path('sign-up/', views.singup, name='signup'),
    path('sign-in/', views.singin, name='signin'),
]