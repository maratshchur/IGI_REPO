import logging
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from.forms import CustomerRegistrationForm, EmployeeRegistrationForm, LoginForm
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger('db_logger')

def home(request):
    logger.info('User accessed home page')
    return render(request, 'users/home.html')

def register(request):
    logger.info('User accessed registration page')
    if request.user.is_authenticated:
        logger.info('User is already authenticated, redirecting to home page')
        return redirect('home')
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            logger.info('Registration form is valid, saving user')
            form.save()
            return redirect('login')
        else:
            logger.info('Registration form is invalid, redirecting to registration page')
            return redirect('client_register')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'users/register_customer.html', {'form': form})

def login(request):
    logger.info('User accessed login page')
    if request.user.is_authenticated:
        logger.info('User is already authenticated, redirecting to home page')
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            logger.info('Login form is valid, authenticating user')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logger.info('User authenticated, logging in')
                login_user(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    logger.info('User logged out')
    logout_user(request)
    return redirect('home')


@login_required
def employee_register(request):
    logger.info('User accessed employee registration page')
    if not request.user.is_superuser:
        logger.warning('Non-superuser tried to access employee registration page')
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            logger.info('Employee registration form is valid, saving user')
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login_user(request, user)
            return redirect('home')
        else:
            logger.info('Employee registration form is invalid, redirecting to employee registration page')
            return redirect('employee_register')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'users/employee_register.html', {'form': form})