from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_profile(models.Model):
  GOALS = (
    ('cut', 'Lose weight'),
    ('maintain', 'Maintain weight'),
    ('gain', 'Bulk up')
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profiles')
  age = models.IntegerField()
  height = models.IntegerField()
  weight = models.IntegerField()
  bmr = models.IntegerField()
  target_weight = models.IntegerField()
  goal = models.CharField(max_length=20, choices=GOALS)

  def __str__(self):
    return self.user.username

class Meal(models.Model):
  MEAL_NAMES = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
  )
  meal_name = models.CharField(max_length=10, choices=MEAL_NAMES)
  total_calories = models.IntegerField()
  total_carbs = models.IntegerField()
  total_fats = models.IntegerField()
  total_proteins = models.IntegerField()
  timestamp = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')

  def __str__(self):
    return self.meal_name

class Food(models.Model):
  name = models.CharField(max_length=200)
  calories = models.IntegerField()
  carbs = models.IntegerField()
  fats = models.IntegerField()
  proteins = models.IntegerField()
  meals = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')

  def __str__(self):
    return self.name

