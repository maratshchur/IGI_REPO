from django.test import TestCase, Client
from django.urls import reverse
from .models import User
from.forms import CustomerRegistrationForm, EmployeeRegistrationForm, LoginForm

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('client_register'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser2',
            'date_of_birth': '1990-01-01',
            'city': 'Minsk',
            'address': 'Some address',
            'phone': '+375(29)123-45-67',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post(reverse('client_register'), data)
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser',
            'password': 'password'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_employee_register_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('employee_register'))
        self.assertEqual(response.status_code, 403)

        self.user.is_superuser = True
        self.user.save()
        response = self.client.get(reverse('employee_register'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser2',
            'date_of_birth': '1990-01-01',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post(reverse('employee_register'), data)
        self.assertEqual(response.status_code, 302)

    def test_invalid_register_view(self):
        response = self.client.get(reverse('client_register'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser2',
            'date_of_birth': '1990-01-01',
            'city': 'Minsk',
            'address': 'Some address',
            'phone': '+375(29)123-45-67',
            'password1': 'password',
            'password2': 'wrong_password'
        }
        response = self.client.post(reverse('client_register'), data)
        self.assertEqual(response.status_code, 302)  

    def test_invalid_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'wrong_username',
            'password': 'password'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200) 

    def test_employee_register_view_without_permission(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('employee_register'))
        self.assertEqual(response.status_code, 403)

    def test_employee_register_view_with_permission(self):
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('employee_register'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view_without_login(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302) 

    def test_home_view_without_login(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_with_login(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)