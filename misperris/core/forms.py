from django import forms

class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")