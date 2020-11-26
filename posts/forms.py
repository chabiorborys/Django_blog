from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(initial='Your name', required=True)
    last_name = forms.CharField(initial='Last name', required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(required=True)

class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Your password', widget=forms.PasswordInput)

def password_validation(value):
    if len(value) < 8:
        raise ValidationError("Password needs to have at least 8 signs.")

class RegisterForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Your password (min 8 signs)', widget=forms.PasswordInput, validators=[password_validation])
    re_password = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Your first name', max_length=20)
    last_name = forms.CharField(label='Your last name', max_length=20)
    email = forms.EmailField(label='E-mail')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] !=cleaned_data['re_password']:
                raise ValidationError("Passwords are not the same.")
        return self.cleaned_data

class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=30)
    description = forms.CharField(label='Description', max_length=200)
    file = forms.FileField()
