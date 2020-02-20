from django.urls import path
from . import views

urlpatterns = [
  path('', views.welcome, name='welcome'), #landing page 
  path('dashboard/<username>/', views.dashboard, name='dashboard'), # user dashboard
  path('search/', views.search, name='search')  # search for food
]