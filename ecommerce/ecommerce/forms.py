from django import forms
from django.contrib.auth import get_user_model


User = get_user_model
class NameForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name'
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'second name'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    content = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'context'
    }))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailInput()
    password = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(label='retype password',widget = forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('uername')
        qs = User.objects.fiter(username= username)
        if qs.exists():
            raise form.ValidationError("User name already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise form.ValidationError("email aready taken") 
        return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match')
        return data


