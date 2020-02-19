from django.urls import path
from . import views

urlpatterns = [
  path('', views.welcome, name='welcome'), #landing page 
  # path('dashboard', views.dashboard, name='dashboard') # user dashboard
]