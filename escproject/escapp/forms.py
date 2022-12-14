from django import forms
from .models import *
from .views import * 
from django.forms import ModelForm
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "register-page-textinput input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "register-page-textinput input"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "register-page-textinput input"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "register-page-textinput input"}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "register-page-textinput input"}))

    class Meta:
        model = Customer
        fields = ["username", "password", "full_name", "password", "confirm_password", "email"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
           raise forms.ValidationError("Username already exists. Please choose another username.")

        return uname 
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "login-page-textinput input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-page-textinput input"})) 


class BookLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "login-page-textinput input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-page-textinput input"})) 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["first_name", "last_name", "phone_number","email", "request", "bank", "credit_card_no","billing_address", "cvv", "expiry"]

