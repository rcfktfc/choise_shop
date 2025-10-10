# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    """
    Форма регистрации пользователя
    """
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите пароль',
            'id': 'password'
        })
    )
    confirm_password = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Повторите пароль',
            'id': 'confirm-password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите имя пользователя',
                'id': 'username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваш email',
                'id': 'email'
            })
        }

    def clean_confirm_password(self):
        """
        Проверка совпадения паролей
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Пароли не совпадают')

        return confirm_password

    def save(self, commit=True):
        """
        Сохранение пользователя с хешированием пароля
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    """
    Форма авторизации пользователя
    """
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите ваше имя',
            'id': 'name'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите пароль',
            'id': 'password'
        })
    )