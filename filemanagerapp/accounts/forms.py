from django import forms 


class LoginForm(forms.Form):
    username = forms.Charfield(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class SugnUpForm(forms.Form): 
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password_confirmsation = forms.CharField(
        max_length=150, widget=forms.PasswordInput
    )