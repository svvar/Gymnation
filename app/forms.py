from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

    class Meta:
        model = User()
        fields = ['firstname', 'lastname', 'phone', 'email', 'password', 'confirm_password']

