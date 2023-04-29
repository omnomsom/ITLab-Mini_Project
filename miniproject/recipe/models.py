from django.db import models
from django import forms
# Create your models here.

class Recipe(models.Model):
  Title = models.CharField(max_length=100)
  Category = models.CharField(max_length=100)
  Recipe = models.CharField(max_length=500)
  class Meta:
    ordering=('Title',)

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    exclude=()
