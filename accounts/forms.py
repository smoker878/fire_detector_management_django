from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Employee


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(label='工號')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput)

class EmployeeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ['username', 'department', 'password1', 'password2']
        labels = {'username': '工號',
                  'department': '部門',
                  'password1': "密碼",
                  'password2': '確認密碼'
                  }
