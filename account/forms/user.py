from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

class UpdateUserForm(forms.Form):
    """docstring for User Form."""
    username = forms.CharField(label='Kullanıcı Adı', min_length=4, max_length=20)
    first_name = forms.CharField(label='Adı', min_length=1, max_length=30, required=False)
    last_name = forms.CharField(label='Soyadı Adı', min_length=1, max_length=30, required=False)
    email = forms.EmailField(label='Eposta Adresi', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)


class CreateUserForm(forms.Form):
    """docstring for User Form."""
    username = forms.CharField(label='Kullanıcı Adı', min_length=4, max_length=20)
    first_name = forms.CharField(label='Adı', min_length=1, max_length=30, required=False)
    last_name = forms.CharField(label='Soyadı Adı', min_length=1, max_length=30, required=False)
    email = forms.EmailField(label='Eposta Adresi', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)
    password1 = forms.CharField(label="Şifre", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Şifre", widget=forms.PasswordInput())

class SignInForm(forms.Form):
    """docstring for User Form."""
    username = forms.CharField(
                label='Kullanıcı Adı',
                widget=forms.TextInput(
                        attrs={'class': "form-control my-3"}
                    )
            )
    password = forms.CharField(
                label="Şifre",
                widget=forms.PasswordInput(
                        attrs={'class': "form-control my-3"}
                    )
            )

def injection(request):
    return {'login_form': SignInForm()}
