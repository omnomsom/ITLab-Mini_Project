from django.shortcuts import render
import pymongo
from recipe.models import Recipe, RecipeForm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def result(request):
    myclient = pymongo.MongoClient("localhost", 27017)
    mydb = myclient["recipeDB"]
    col1 = mydb["Categories"]
    col2 = mydb["Recipes"]
    if request.method == 'POST':
        print(request.POST)
        selected_checkboxes = []
        checkbox_names = ['Potato', 'Cabbage', 'Onions', 'Tomato', 'French Beans', 'Beetroot', 'Garlic', 'Basmati Rice', 'Paneer', 'Curd', 'Chicken', 'Green Chilli', 'Cream', 'Butter', 'Fruits', 'Capsicum', 'Bread', 'Lemon', 'Maida', 'Cheese']
        for checkbox_name in checkbox_names:
            if checkbox_name in request.POST:
                selected_checkboxes.append(checkbox_name)
        
        recipes = []
        for x in col2.find({'Ingredients':{'$all':selected_checkboxes}}):
            r = {'title':x['Title'], 'img':x['Image'],'det':x['Recipe']}
            recipes.append(r)
 
        context = {
            'selected_checkboxes': selected_checkboxes,
            'recipes' : recipes
        }
        return render(request, 'result.html', context)
    
    return render(request, 'test.html')

def add(request):
  entries = Recipe.objects.all()[:10]
  return render(request, 'add.html', {'entries':entries,'title':RecipeForm()['Title'], 'category':RecipeForm()['Category'], 'recipe':RecipeForm()['Recipe']})

def add_recipe(request):
   if request.method == 'POST':
      form = RecipeForm(request.POST)
      if form.is_valid():
        entry = form.save()
   return HttpResponseRedirect('/')

def show_recipe(request):
  entries = Recipe.objects.all()
  return render(request, 'show.html', {'entries':entries})


