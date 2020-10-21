from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(initial='Your name', required=True)
    last_name = forms.CharField(initial='Last name', required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(required=True)
