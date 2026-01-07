from django import forms
from .models import LoginModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '@Seu_nome123'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '12341234'
            }),
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.startswith('@'):
            raise forms.ValidationError (
                'O nome de usuário deve ter um @ no começo'
            )
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError (
                'A senha deve ter no mínimo 8 dígitos'
            )
        return password

class CadastroForm (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.startswith('@'):
            raise forms.ValidationError (
                'O nome de usuário deve ter um @ no começo'
            )
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError (
                'A senha deve ter no mínimo 8 dígitos'
            )
        return password