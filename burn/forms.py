from django import forms
from .models import User_profile
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('age', 'gender', 'height', 'weight', 'target_weight', 'goal')


# class SignUpForm(UserCreationForm):
#     name = forms.CharField(max_length=30, required=False)
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     class Meta:
#         model = User
#         fields = ('username', 'name', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
