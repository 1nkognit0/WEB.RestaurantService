from django.shortcuts import render, redirect
from django.contrib import auth

from users.forms import UserAuthorizationForm, RegistrationForm


def login_view(request):
    if request.method == 'POST':
        login_form = UserAuthorizationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth.login(request, user)
            return redirect(get_role_url(user.role))
    else:
        login_form = UserAuthorizationForm()
    return render(request, 'users/login.html', {'form': login_form, 'title': 'Авторизация'})

def registration_view(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('login')
    else:
        reg_form = RegistrationForm()
    return render(request, 'users/reg.html', {'form': reg_form, 'title': 'Регистрация'})

def get_role_url(role):
    role_urls = {
        'admin': 'admin',
        'waiter': 'waiter',
        'chef': 'orders',
    }
    return role_urls.get(role)

