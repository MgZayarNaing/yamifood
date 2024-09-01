from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('menu/', views.menu_list, name='menu_list'),

]