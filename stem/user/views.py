from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Аккаунт створено!")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Невірний логін або пароль!")
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')