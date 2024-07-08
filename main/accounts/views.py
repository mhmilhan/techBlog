from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)



def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Ensure the user has a profile
            profile, created = Profile.objects.get_or_create(user=user)
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('index')