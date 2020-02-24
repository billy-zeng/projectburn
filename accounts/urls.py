from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'), #signup1
    path('login/', views.login, name='login'), #login page
    path('logout/', views.logout, name='logout'), #logout page
]