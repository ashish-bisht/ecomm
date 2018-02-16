from django import forms

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
    password = forms.CharField()
    password2 = forms.CharField()   

