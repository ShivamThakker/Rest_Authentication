from django.forms import ModelForm
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from account.models import Account
from django import forms

# widget=forms.Textarea(attrs={EmailField})
class RegisterForm(forms.ModelForm):
    email = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)
    class Meta:
        model = Account
        fields = ["email", "username", "password", "confirm_password"]

    