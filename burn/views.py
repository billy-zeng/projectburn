from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Food, User_profile
import requests
from .forms import ProfileForm, SearchForm, FoodForm
from django.http import HttpResponse

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
    add_food_form = FoodForm()

    meal = request.POST.get('meal')
    timestamp = request.POST.get('timestamp')

    if meal is not None and timestamp is not None:
      add_food_form = FoodForm(request.POST)

    # Handle add food (create new database entry)
    if add_food_form.is_valid():
      food = add_food_form.save(commit=False)
      food.name = request.POST.get('food_name')
      food.calories = request.POST.get('food_calories')
      food.meal.total_calories += float(food.calories)
      food.carbs = request.POST.get('food_carbs')
      food.meal.total_carbs += float(food.carbs)
      food.fats = request.POST.get('food_fats')
      food.meal.total_fats += float(food.fats)
      food.proteins = request.POST.get('food_proteins')
      food.meal.total_proteins += float(food.proteins)
      food.image = request.POST.get('food_img')
      food.save()
      food.meal.save()
      return redirect('dashboard')

    # Handle search food
    if form.is_valid():
      query = form.cleaned_data['search']

      # nutrionix api
      response = requests.post(
        "https://trackapi.nutritionix.com/v2/natural/nutrients",
        headers = {
          'Content-Type': 'application/json',
          "x-app-id": "93bf5046",
          "x-app-key": "5f48f0fc898a6ab5caaeac3bdfd58e79"
        },
        json = {"query": query}
      )
      data = response.json()
      food_data = []
      if 'foods' in data:
        for item in data['foods']:
          food_obj = {
            'food_name': item['food_name'],
            'serving': item['serving_weight_grams'],
            'calories': item['nf_calories'],
            'protein': item['nf_protein'],
            'fat': item['nf_total_fat'],
            'carbs': item['nf_total_carbohydrate'],
            'img_url': item['photo']['thumb']
          }
          food_data.append(food_obj)
      else:
        food_data = None

      if food_data == None:
        context = {'form': form, 'ip': data, 'error': "No foods found, please try again"}
      else:
        context = {'form': form, 'ip': data, 'food_data': food_data, 'add_food_form': add_food_form}
      return render(request, 'search.html', context)
  else:
    form = SearchForm()
    add_food_form = FoodForm()

  # if add_food_form.is_valid():
  #   return render(request, 'dashboard')
  # else:
  return render(request, 'search.html', {'form': form, 'add_food_form': add_food_form})


def create_profile(request):
  user = request.user
  form = ProfileForm(request.POST)
  if form.is_valid():
    user_profile = form.save(commit=False)
    if user_profile.gender == 'Male':
      user_profile.bmr = round(66.47 + (6.24 * user_profile.weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
      user_profile.target_bmr = round(66.47 + (6.24 * user_profile.target_weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
    else:
      user_profile.bmr = round(655.1 + (4.35 * user_profile.weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age))
      user_profile.target_bmr = round(655.1 + (4.35 * user_profile.target_weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age)) 
    user_profile.user = user
    user_profile.save()
    breakfast = Meal.objects.create(meal_name='Breakfast', user=user)
    breakfast.save()
    snacks = Meal.objects.create(meal_name='Snacks', user=user)
    snacks.save()
    lunch = Meal.objects.create(meal_name='Lunch', user=user)
    lunch.save()
    dinner = Meal.objects.create(meal_name='Dinner', user=user)
    dinner.save()
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

def add_food(request):
  user = request.user
  user_profile = User_profile.objects.get(user=user)
  if request.method == 'POST':
    form = FoodForm(request.POST)
    if form.is_valid():
      # food.meal = request.POST['meal']
      # food.timestamp = request.POST['timestamp']

      # food_data = request.POST.get('food_data')
      # food_name = request.POST.get('food_name')
      # food_calories = request.POST.get('food_calories')
      # food_carbs = request.POST.get('food_carbs')
      # food_fats = request.POST.get('food_fats')
      # food_proteins = request.POST.get('food_proteins')
      # print(food_name)
      # print(food_calories)
      # print(food_carbs)
      # print(food_fats)
      # print(food_proteins)

      food = form.save(commit=False)
      food.name = 'test name 2'
      food.calories = 1
      food.carbs = 2
      food.fats = 3
      food.proteins = 4
      food.save()
      return redirect(request, 'dashboard/')
  else:
    form = FoodForm()
  return redirect(request, 'dashboard/')


  
# reset (for new day)
def clear_foods(request):
  user = request.user
  meals = Meal.objects.filter(user=user)
  for meal in meals:
    foods = Food.objects.filter(meal=meal).delete()
    meal.total_calories = 0
    meal.total_carbs = 0
    meal.total_fats = 0
    meal.total_proteins = 0
    meal.save()
  return HttpResponse('reset!')
