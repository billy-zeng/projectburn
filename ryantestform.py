from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = Userfields = ('name', 'height', 'weight', 'age', 'isMale', 'bmr', 'targetweight', 'goal')




class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
