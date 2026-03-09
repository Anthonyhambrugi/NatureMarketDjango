from django import forms
from django.contrib.auth.models import User
from cadastro.models import UserMod

class EditarPerfilForm(forms.ModelForm):
    fotodeperfil = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
        }


        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            perfil = UserMod.objects.filter(user=self.instance).first()
            if perfil:
                self.fields['fotodeperfil'].initial = perfil.fotodeperfil
                self.fields['bio'].initial = perfil.bio
