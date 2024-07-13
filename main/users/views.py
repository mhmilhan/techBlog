from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import Profile
from users.forms import AddUserForm, EditUserForm


# Create your views here.
@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'users/user.html', context)

def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context = {
        'form': form,
    }
    return render(request, 'users/add_user.html', context)


def edit_user(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'users/edit_user.html', context)

def is_superuser_or_staff(user):
    return user.is_superuser or user.is_staff

@user_passes_test(is_superuser_or_staff)
def delete_user(request, username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return redirect('users')
    except User.DoesNotExist:
        # Handle the case where the user does not exist
        return redirect('users')


