from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),  # search for food
    path('create_profile/', views.create_profile, name='create_profile'), # create profile
    path('edit_profile/', views.edit_profile, name='edit_profile') # edit profile
]
=======
  path('', views.home, name='home'),
  # path('', views.welcome, name='welcome'), #landing page 
  path('dashboard/', views.dashboard, name='dashboard'), # user dashboard
  path('search/', views.search, name='search'),  # search for food
  path('create_profile/', views.create_profile, name='create_profile'), # create profile  
  path('edit_profile/', views.edit_profile, name='edit_profile'), # edit profile
  # path('search_food/', views.search_food, name='search_food'),
]

>>>>>>> submaster
