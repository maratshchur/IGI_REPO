from datetime import datetime, timezone
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta
from .models import Customer, Employee, User
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate


phone_regex = RegexValidator(
    regex=r'^\+375(\s+)?\(?(17|29|33|44)\)?(\s+)?[0-9]{3}-[0-9]{2}-[0-9]{2}$',
    message='Invalid phone number format. Please use +375(xx)xxx-xx-xx'
)

class CustomerRegistrationForm(UserCreationForm):
    city = forms.CharField(max_length=100, label='Город')
    address = forms.CharField(max_length=200, label='Адрес')
    phone = forms.CharField(max_length=20, label='Мобильный телефон', validators=[phone_regex])

    class Meta:
        model = User
        fields = ('username', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        customer = Customer(user=user, city=self.cleaned_data['city'], address=self.cleaned_data['address'], phone=self.cleaned_data['phone'])
        customer.save()
        return user

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        age = relativedelta(datetime.now().date(),date_of_birth).years
        if age < 18:
            raise forms.ValidationError(_('You must be at least 18 years old to register.'))
        return date_of_birth
    
class EmployeeRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        employee = Employee(user=user)
        employee.save()
        return user

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        age = relativedelta( datetime.now().date(), date_of_birth).years
        if age < 18:
            raise forms.ValidationError(_('You must be at least 18 years old to register.'))
        return date_of_birth
    
    

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=255)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Неверное имя пользователя или пароль')
        return self.cleaned_data