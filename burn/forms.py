from django import forms
from .models import User_profile, Meal, Food

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('age', 'gender', 'height', 'weight', 'target_weight', 'goal')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'search_form'}), label='')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('meal','timestamp')
        labels = {
            'meal': 'Meal',
            'timestamp': 'Time'
        }
