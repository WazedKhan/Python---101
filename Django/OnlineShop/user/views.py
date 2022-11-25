from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
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
    return render(request, 'registration.html', {'form':form})


