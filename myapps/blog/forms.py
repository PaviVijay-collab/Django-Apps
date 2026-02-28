from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length= 50, required=False)
    email = forms.EmailField(label="E-Mail")
    message = forms.CharField(label="Message")
    subject = forms.CharField(label="Subject")