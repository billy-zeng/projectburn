from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Food, User_profile
import requests
from .forms import ProfileForm
from requests_auth import Basic

# 'https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={your app_id}&app_key={your app_key}'
def home(request):
    # response = requests.get('https://foodapi.calorieking.com/v1', auth=('user', ''))
    response = requests.get('https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={9b687b99}&app_key={bc5f2cc77eb479801a3ec37121ccc27a}')
    data = response.json()
    print(response)
    return render(request, 'home.html', {
        'ip': data
    })


# 'https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={your app_id}&app_key={your app_key}'
def home(request):
  # response = requests.get('https://foodapi.calorieking.com/v1', auth=('user', ''))
  response = requests.get('https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={9b687b99}&app_key={bc5f2cc77eb479801a3ec37121ccc27a}')
  data = response.json()
  print(response)
  return render(request, 'home.html', {
    'ip': data
  })

def welcome(request):
  return render(request, 'welcome.html')

def dashboard(request):
  user = request.user
  user_profile = User_profile.objects.get(user=user)
  meals = Meal.objects.filter(user=user)
  return render(request, 'dashboard.html', {'username': user.username, 'meals': meals, 'user_profile': user_profile})

def search(request):
  return render(request, 'search.html')

def create_profile(request):
  user = request.user
  form = ProfileForm(request.POST)
  if form.is_valid():
    user_profile = form.save(commit=False)
    if user_profile.gender == 'Male':
      user_profile.bmr = round(66.47 + (6.24 * user_profile.weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
    else:
      user_profile.bmr = round(655.1 + (4.35 * user_profile.weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age))
    user_profile.user = user
    user_profile.save()
    return redirect('dashboard')
  else:
    form = ProfileForm()
  context = {'form': form, 'header': "Set up your profile"}
  return render(request, 'profile_form.html', context)

def edit_profile(request):
  user = request.user
  user_profile = User_profile.objects.get(user=user)
  if request.method == 'POST':
    form = ProfileForm(request.POST, instance=user_profile)
    if form.is_valid():
      user_profile = form.save(commit=False)
      if user_profile.gender == 'Male':
        user_profile.bmr = round(66.47 + (6.24 * user_profile.weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
      else:
        user_profile.bmr = round(655.1 + (4.35 * user_profile.weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age))
      user_profile.save()
      return redirect('dashboard')
  else:
    form = ProfileForm(instance=user_profile)
  context = {'form': form, 'header': "Edit your profile"}
  return render(request, 'profile_form.html', context)


# def search(request):
#   # response = requests.get('https://foodapi.calorieking.com/v1', auth=('user', ''))
#   response = requests.get('https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id=9b687b99&app_key=bc5f2cc77eb479801a3ec37121ccc27a')
#   data = response.json()
#   print(response)
#   return render(request, 'search.html', {
#       'ip': data
#   })
