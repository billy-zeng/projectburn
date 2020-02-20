from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Meal, Food, User_profile
import requests

# Create your views here.

def welcome(request):
  return render(request, 'welcome.html')

def dashboard(request, username):
  user = User.objects.get(username=username)
  user_profile = User_profile.objects.get(user=user)
  meals = Meal.objects.filter(user=user)
  return render(request, 'dashboard.html', {'username': username, 'meals': meals, 'user_profile': user_profile})

# def search(request):
#   return render(request, 'search.html')
