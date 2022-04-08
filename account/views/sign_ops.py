
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from account.models import CustomUserModel
from account.forms import CreateUserForm, SignInForm


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
        return redirect('home_url')


@login_required(login_url='/')
def sign_out(request):
    logout(request)
    return redirect('home_url')

def sign_up(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if CustomUserModel.objects.filter(username=cd['username']).exists():
                messages.error(request, f"{cd['username']} isminde bir kullanıcı zaten var")
                return redirect('sign_up_url')
            elif cd['password1'] == cd['password1']:
                new_user = CustomUserModel()
                new_user.username = cd['username']
                new_user.first_name = cd['first_name']
                new_user.last_name = cd['last_name']
                new_user.email = cd['email']
                if request.FILES:
                    new_user.avatar = request.FILES['avatar']
                new_user.password = make_password(cd['password1'])
                new_user.save()
                login(request, new_user)
                messages.success(request, 'Yeni kullanıcı oluşturuldu.')
                return redirect('update_user_url')
    else:
        form = CreateUserForm()
    context={
        'form' : form
    }
    return render(request, 'sign_up.html', context)
