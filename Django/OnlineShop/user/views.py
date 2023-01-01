from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from user.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def account(request):
    return HttpResponse('')


def registration(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully')
        else:
            messages.error(request, f'Couldnt created the account')
    form = UserRegisterForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password= request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            messages.success(request, f'Login successfully')
            return redirect('category-list')
        messages.error(request, 'Username or Password Invalid')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('category-list')
