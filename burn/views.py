from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Meal, Food, User_profile

# Create your views here.

def welcome(request):
  return render(request, 'welcome.html')

def dashboard(request, username):
  user = User.objects.get(username=username)
  user_profile = User_profile.objects.get(user=user)
  meals = Meal.objects.filter(user=user)
  return render(request, 'dashboard.html', {'username': username, 'meals': meals, 'user_profile': user_profile})

# #user metrics
# def post_user_metrics(request):
#     form = UserForm(request.POST)
#     if form.is_valid():
#         user = User(
#             name=form.cleaned_data['name'],
#             height=form.cleaned_data['height'],
#             weight=form.cleaned_data['weight'],
#             age=form.cleaned_data['age'],
#             isMale=form.boolean_field(default=True),
#             bmr=bmr(),
#             targetweight=form.cleaned_data['targetweight'],
#             goal=form.as_table['bulk', 'maintain_weight', 'lose_weight'],
#         )

#         User = form.save(commit = False)
#         User.save()

# #daily calorie intake calculation
# def bmr():
# # Harris-Benedict Equation
#     if User.isMale:
#         bmr = 66.47 + (6.24 * User.weight) + (12.7 * User.height) - (6.755 * User.age)
#     else:
#         bmr = 655.1 + (4.35 * User.weight) + (4.7 * User.height) - (4.7 * User.age)

#     bmr = round(bmr)
#     print(bmr)