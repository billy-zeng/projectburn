from django import forms
from .models import User_profile
from .models import Meal
from .models import Food
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('age', 'gender', 'height', 'weight', 'target_weight', 'goal')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Foods')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('meal','timestamp')
