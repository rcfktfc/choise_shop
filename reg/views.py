# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegistrationForm, UserLoginForm


def registration(request):
    """
    Обработка регистрации пользователя
    """
    # Если пользователь уже авторизован, перенаправляем на главную
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Автоматический вход после регистрации
            login(request, user)
            messages.success(request, f'Регистрация прошла успешно! Добро пожаловать, {user.username}!')
            return redirect('/')  # Замените 'home' на ваш URL
        else:
            # Показываем ошибки формы
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserRegistrationForm()

    return render(request, 'reg/registr.html', {'form': form})


def reg(request):
    """
    Обработка авторизации пользователя
    """
    # Если пользователь уже авторизован, перенаправляем на главную
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.username}!')

                # Перенаправление на страницу, с которой пришли, или на главную
                return redirect('/')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = UserLoginForm()

    return render(request, 'reg/auth.html', {'form': form})


def logout_view(request):
    """
    Выход пользователя
    """
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('login')