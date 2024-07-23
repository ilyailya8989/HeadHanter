from django.urls import path
from user import views

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('sign-in/', views.signin, name='signin'),
]