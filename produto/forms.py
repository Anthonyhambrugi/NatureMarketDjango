from django import forms
from .models import CadItmModel

class CadItmForm(forms.ModelForm):
    class Meta:
        model = CadItmModel
        fields = '__all__'
        exclude = ['autor']
