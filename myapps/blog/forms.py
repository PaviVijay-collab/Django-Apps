from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password", max_length=100, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')       
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid Username And Password")                                           
            

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No User Register with this Email")