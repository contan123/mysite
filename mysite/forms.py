from django import forms

class LoginForm(forms.Form):
    usename = forms.CharField()
    password = forms.CharField()