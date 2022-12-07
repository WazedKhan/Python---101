from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from user.forms import UserRegisterForm


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
            return redirect('category-list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('category-list')
