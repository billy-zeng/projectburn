from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),  # search for food
    path('create_profile/', views.create_profile, name='create_profile'), # create profile
    path('edit_profile/', views.edit_profile, name='edit_profile'), # edit profile
    path('clear_foods/', views.clear_foods, name='clear_foods')
]
