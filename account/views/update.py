import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.models import model_to_dict

from account.forms import UpdateUserForm
from account.models import CustomUserModel


@login_required(login_url='/')
def update_user(request):
    form = UpdateUserForm(
        request.POST or None,
        request.FILES or None,
        initial=model_to_dict(request.user),
    )
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            request.user.username = cd['username']
            request.user.first_name = cd['first_name']
            request.user.last_name = cd['last_name']
            request.user.email = cd['email']
            if request.FILES:
                if request.user.avatar:
                    os.remove(request.user.avatar.path)
                request.user.avatar = request.FILES['avatar']
            request.user.save()
            return redirect('update_user_url')
    context={
        'form' : form,
    }
    return render(request, 'update_user.html', context)



@login_required(login_url='/')
def change_pwd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifre başarıyla değiştirildi.')
            return redirect('change_pwd_url')
    else:
        form = PasswordChangeForm(request.user)

    context={
        'form' : form
    }
    return render(request, 'change_pwd.html', context)
