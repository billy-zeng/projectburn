from django.contrib import admin
from .models import User_profile, Meal, Food

# Register your models here.
admin.site.register(User_profile)
admin.site.register(Meal)
admin.site.register(Food)