from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Food, User_profile
import requests
from .forms import ProfileForm, SearchForm
# from requests_auth import Basic

# 'https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={your app_id}&app_key={your app_key}'
def home(request):
  # response = requests.get('https://foodapi.calorieking.com/v1', auth=('user', ''))
  response = requests.get('https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id=9b687b99&app_key=bc5f2cc77eb479801a3ec37121ccc27a')
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
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      query = form.cleaned_data
      response = requests.get(f'https://api.edamam.com/api/food-database/parser?ingr={query}&app_id=9b687b99&app_key=bc5f2cc77eb479801a3ec37121ccc27a')
      data = response.json()

      food_data = []
      for item in data['hints']:
        food_obj = {
          'label': '',
          'calories': '',
          'protein': '',
          'fat': '',
          'carbs': ''
        }
        if 'label' in item['food']:
          food_obj['label'] = item['food']['label']
        if 'ENERC_KCAL' in item['food']['nutrients']:
          food_obj['calories'] = item['food']['nutrients']['ENERC_KCAL']
        if 'PROCNT' in item['food']['nutrients']:
          food_obj['protein'] = item['food']['nutrients']['PROCNT']
        if 'FAT' in item['food']['nutrients']:
          food_obj['fat'] = item['food']['nutrients']['FAT']
        if 'CHOCDF' in item['food']['nutrients']:
          food_obj['carbs'] = item['food']['nutrients']['CHOCDF']
        food_data.append(food_obj)
      print(food_data)

      context = {'form': form, 'ip': data, 'food_data': food_data}
      return render(request, 'search.html', context)
  else:
    form = SearchForm()
  return render(request, 'search.html', {'form': form})


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
