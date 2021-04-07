from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django import forms
from dal import autocomplete
from .models import *


class RegisterForm(UserCreationForm):
    profiletype = forms.ModelChoiceField(queryset=ProfileType.objects.all())
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'new-password', 'placeholder': 'Confirm Password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = False
    


class LoginForm(AuthenticationForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': False, 'class':'form-control', 'placeholder': 'Username'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'profile_type': forms.Select(attrs={'class': 'form-control'}),
            'skills_have':autocomplete.ModelSelect2Multiple(url='skill-autocomplete', attrs={'class': 'form-control'}),
            'skills_wanted':autocomplete.ModelSelect2Multiple(url='skill-autocomplete', attrs={'class': 'form-control'} ),
        }


class AutocompleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_type', 'location', 'human_language', 'skills_have', 'skills_wanted']
        widgets = {
            'skills_have':autocomplete.ModelSelect2Multiple(url='skill-autocomplete'),
            'skills_wanted':autocomplete.ModelSelect2Multiple(url='skill-autocomplete'),
        }


