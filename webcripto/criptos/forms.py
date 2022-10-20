from django import forms
from .models import Cripto

class CriptoForm(forms.ModelForm):
    class Meta:
        model= Cripto
        fields= ['icon','image','name','sigle','unids','preci','description','codeFont','web',]