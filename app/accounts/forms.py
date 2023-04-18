from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from django.core.validators import EmailValidator

import re

User = get_user_model()

class RegisterForm(forms.Form):

    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(error_messages={"invalid": "Введіть правильну електронну адресу"})
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User()
        fields = ['firstname', 'lastname', 'phone', 'email', 'password', 'confirm_password']

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        if not re.match(r'[А-ЯҐЄІЇа-яґєії\-\'\`]+', firstname):
            raise forms.ValidationError("Введіть ім'я українською")
        return firstname.capitalize()

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        if not re.match(r'[А-ЯҐЄІЇа-яґєії\-\'\`]+', lastname):
            raise forms.ValidationError("Введіть прізвище українською")
        return lastname.capitalize()

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\d{12}$', phone):
            raise forms.ValidationError("Введіть номер телефону (12 цифр)")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)

        try:
            EmailValidator(email)
        except ValidationError:
            print("mamamammamamama")
            raise forms.ValidationError("Введіть правильну електронну адресу!")

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Електонна адреса вже зайнята")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Паролі не співпадають!')

        return password


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()

    photo = forms.ImageField()

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    is_staff = forms.BooleanField(required=False)  # a admin user; non super-user
    is_superuser = forms.BooleanField(required=False)  # a superuser


    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'email', 'photo', 'password', 'confirm_password']

    def validate_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return confirm_password

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()

    photo = forms.ImageField()

    password = ReadOnlyPasswordHashField()

    is_staff = forms.BooleanField(required=False)  # a admin user; non super-user
    is_superuser = forms.BooleanField(required=False)  # a superuser


    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'email', 'photo', 'password', 'is_staff', 'is_superuser']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
