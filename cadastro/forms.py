from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
