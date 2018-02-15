from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    second_name = forms.CharField(label='Second name',max_length=100)
    email = forms.CharField(label='email',max_length=100)
    content = forms.CharField()