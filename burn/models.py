from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_profile(models.Model):
  GOALS = (
    ('Lose weight', 'Lose weight'),
    ('Maintain weight', 'Maintain weight'),
    ('Bulk up', 'Bulk up')
  )
  GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profiles')
  age = models.IntegerField()
  gender = models.CharField(max_length=6, choices=GENDER)
  height = models.IntegerField()
  weight = models.IntegerField()
  bmr = models.IntegerField()
  target_bmr = models.IntegerField()
  target_weight = models.IntegerField()
  goal = models.CharField(max_length=20, choices=GOALS)

  def __str__(self):
    return self.user.username

class Meal(models.Model):
  MEAL_NAMES = (
    ('Breakfast', 'Breakfast'),
    ('Snacks', 'Snacks'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snacks', 'Snacks')
  )
  meal_name = models.CharField(max_length=10, choices=MEAL_NAMES)
  total_calories = models.FloatField(default=0)
  total_carbs = models.FloatField(default=0)
  total_fats = models.FloatField(default=0)
  total_proteins = models.FloatField(default=0)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')

  def __str__(self):
    return self.meal_name

class Food(models.Model):
  name = models.CharField(max_length=200)
  calories = models.FloatField()
  carbs = models.FloatField()
  fats = models.FloatField()
  proteins = models.FloatField()
  timestamp = models.DateTimeField()
  meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
  def __str__(self):
    return self.name
