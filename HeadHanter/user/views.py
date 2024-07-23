from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import SignUpForm, SignInForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('vacancy_list')
    sign_form = SignUpForm()
    if request.method == 'POST':
        sign_form = SignUpForm(request.POST)
        if sign_form.is_valid():
            user = sign_form.save()
            login(request, user)
            return redirect('vacancy_list')
    return render(request, 'user/registration.html', {'form': sign_form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('vacancy_list')
    sign_form = SignInForm()
    if request.method == 'POST':
        sign_form = SignInForm(request.POST)
        if sign_form.is_valid():
            user_name = sign_form.cleaned_data['username']
            password = sign_form.cleaned_data['password']
            user = authenticate(request, username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('vacancy_list')
    return render(request, 'user/autorisation.html', {'form': sign_form})
