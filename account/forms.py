from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator

from .models import Member, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    error_messages = {
        'email': {
            'unique': "This email address is already in use. Please use a different email address.",
        },
        'password2': {
            'password_mismatch': "The passwords don't match.",
        },
    }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(self.error_messages['email']['unique'])
        return email

class UserRegistrationForm(CustomUserCreationForm):
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(self.error_messages['password2']['password_mismatch'])
        return cd['password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'sex', 'phone_number', 'email', 'age']
