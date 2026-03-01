from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class EditarPerfilForm(forms.ModelForm):
    fotodeperfil = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]

        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            perfil = Perfil.objects.filter(user=self.instance).first()
            if perfil:
                self.fields['fotodeperfil'].initial = perfil.fotodeperfil
                self.fields['bio'].initial = perfil.bio
