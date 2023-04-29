from django.contrib import admin
import site
from recipe.models import Recipe
from recipe import models
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Category')
admin.site.register(models.Recipe, RecipeAdmin)
