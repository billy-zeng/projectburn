from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Meal, Food, User_profile
import requests
from .forms import ProfileForm, SearchForm, FoodForm
from django.contrib.auth.decorators import login_required

def welcome(request):
  return render(request, 'welcome.html')

@login_required
def dashboard(request):
  user = request.user
  user_profile = User_profile.objects.get(user=user)
  meals = Meal.objects.filter(user=user)

  # calculate target macros
  if user_profile.goal == 'Bulk up':
    target_calories = user_profile.target_bmr*1.4
  elif user_profile.goal == 'Lose weight':
    target_calories = user_profile.target_bmr
  else:
    target_calories = user_profile.target_bmr*1.2
  target_proteins = user_profile.target_weight
  target_fats = target_calories/4/9
  target_carbs = (target_calories - target_proteins*4 - target_fats*9)/4

  # initiate current macro variables
  current_calories = 0
  current_carbs = 0
  current_fats = 0
  current_proteins = 0

  # calculate current macros
  for meal in meals:
    current_calories += meal.total_calories
    current_carbs += meal.total_carbs
    current_fats += meal.total_fats
    current_proteins += meal.total_proteins

  # calculate current/target macro ratio 
  percent_calories = 100*current_calories/target_calories
  percent_carbs = 100*current_carbs/target_carbs
  percent_fats = 100*current_fats/target_fats
  percent_proteins = 100*current_proteins/target_proteins

  context = {'username': user.username, 'meals': meals, 'user_profile': user_profile, 
  'percent_calories': percent_calories, 'percent_carbs': percent_carbs, 'percent_fats': percent_fats, 'percent_proteins': percent_proteins, 
  'target_calories': target_calories, 'target_carbs': target_carbs, 'target_fats': target_fats, 'target_proteins': target_proteins}
  
  return render(request, 'dashboard.html', context)

@login_required
def search(request):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    add_food_form = FoodForm()
    add_food_form.fields['meal'].queryset = Meal.objects.filter(user=request.user)

    meal = request.POST.get('meal')
    timestamp = request.POST.get('timestamp')

    if meal is not None and timestamp is not None:
      add_food_form = FoodForm(request.POST)

    # Handle add food (create new database entry)
    if add_food_form.is_valid():
      # create new food entry in database with form and card values
      food = add_food_form.save(commit=False)
      food.name = request.POST.get('food_name')
      food.calories = request.POST.get('food_calories')
      food.carbs = request.POST.get('food_carbs')
      food.fats = request.POST.get('food_fats')
      food.proteins = request.POST.get('food_proteins')
      food.image = request.POST.get('food_img')

      # update meal total macros
      food.meal.total_calories += float(food.calories)
      food.meal.total_carbs += float(food.carbs)
      food.meal.total_fats += float(food.fats)
      food.meal.total_proteins += float(food.proteins)

      # commit changes to database
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
            'proteins': item['nf_protein'],
            'fats': item['nf_total_fat'],
            'carbs': item['nf_total_carbohydrate'],
            'img_url': item['photo']['thumb']
          }
          food_data.append(food_obj)
      else:
        food_data = None

      if food_data == None:
        context = {'form': form, 'error': "No foods found, please try again"}
      else:
        context = {'form': form, 'food_data': food_data, 'add_food_form': add_food_form}
      return render(request, 'search.html', context)
  else:
    form = SearchForm()
    add_food_form = FoodForm()

  return render(request, 'search.html', {'form': form, 'add_food_form': add_food_form})

@login_required
def create_profile(request):
  user = request.user
  form = ProfileForm(request.POST)
  if form.is_valid():
    # set up user profile according to form data and calculate bmr
    user_profile = form.save(commit=False)
    if user_profile.gender == 'Male':
      user_profile.bmr = round(66.47 + (6.24 * user_profile.weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
      user_profile.target_bmr = round(66.47 + (6.24 * user_profile.target_weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
    else:
      user_profile.bmr = round(655.1 + (4.35 * user_profile.weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age))
      user_profile.target_bmr = round(655.1 + (4.35 * user_profile.target_weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age)) 
    user_profile.user = user
    user_profile.save()

    # initalize user's meals
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

@login_required
def edit_profile(request):
  user = request.user
  user_profile = User_profile.objects.get(user=user)
  if request.method == 'POST':
    form = ProfileForm(request.POST, instance=user_profile)
    if form.is_valid():
      user_profile = form.save(commit=False)
      if user_profile.gender == 'Male':
        user_profile.bmr = round(66.47 + (6.24 * user_profile.weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
        user_profile.target_bmr = round(66.47 + (6.24 * user_profile.target_weight) + (12.7 * user_profile.height) - (6.755 * user_profile.age))
      else:
        user_profile.bmr = round(655.1 + (4.35 * user_profile.weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age))
        user_profile.target_bmr = round(655.1 + (4.35 * user_profile.target_weight) + (4.7 * user_profile.height) - (4.7 * user_profile.age)) 
      user_profile.save()
      return redirect('dashboard')
  else:
    form = ProfileForm(instance=user_profile)
  context = {'form': form, 'header': "Edit your profile"}
  return render(request, 'profile_form.html', context)

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
  return redirect('dashboard')
