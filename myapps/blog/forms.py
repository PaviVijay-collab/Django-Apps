from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length= 50, required=True)
    email = forms.EmailField(label="E-Mail", required=True)
    message = forms.CharField(label="Message", required=True)
    # subject = forms.CharField(label="Subject", required=True)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)
    confirm_password = forms.CharField(label='Confirm Password', max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password Mismatch")

    
