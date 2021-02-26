from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import (
        authenticate,
        get_user_model,
        login,
        logout,
        )


class UserAccountForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), required=False, label='')
    last_name = forms.CharField(widget=forms.TextInput(), required=False, label='')
    email = forms.CharField(widget=forms.TextInput(), required=False, label='')

    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'email',
                ]


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(), required=False, label='')
    address = forms.CharField(widget=forms.TextInput(), required=False, label='')
    country = forms.CharField(widget=forms.TextInput(), required=False, label='')

    class Meta:
        model = Profile
        fields = [
                'phone',
                'address',
                'country',
                ]                



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), label='* ИМЯ ПОЛЬЗОВАТЕЛЯ')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}), label='* ПАРОЛЬ')

    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            if not user:
                raise forms.ValidationError('Такой пользователь не зарегестрирован')
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
            if not user.is_active:
                raise forms.ValidationError('Пользователь не активирован')
        return super().clean(*args, **kwargs)
            

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), label='* ИМЯ ПОЛЬЗОВАТЕЛЯ')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', }), label='* ЕМЕЙЛ')
    email2 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', }), label='* Подтвердите ЕМЕЙЛ')
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}), label='* ПАРОЛЬ')
    
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Емайлы не совпадают')
        return email
    
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'email2',
                'password',
                ]
