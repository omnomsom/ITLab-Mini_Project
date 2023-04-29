from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('add/', views.add, name='add'),
    path('recipe/add_recipe/', views.add_recipe, name='add_recipe'),
    path('show/', views.show_recipe, name='show_recipe'),
]
