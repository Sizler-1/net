from django import forms
from .models import BorderCrossing, Vaccine

class BorderCrossingForm(forms.ModelForm):
    class Meta:
        model = BorderCrossing
        fields = '__all__'

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'date_administered']


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())
