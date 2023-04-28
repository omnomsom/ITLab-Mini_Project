from django.shortcuts import render
import pymongo

def index(request):
    return render(request, 'index.html')

def result(request):
    myclient = pymongo.MongoClient("localhost", 27017)
    mydb = myclient["recipeDB"]
    col1 = mydb["Categories"]
    col2 = mydb["Recipes"]
    if request.method == 'POST':
        selected_checkboxes = []
        checkbox_names = ['potato', 'cauli', 'onion']
        for checkbox_name in checkbox_names:
            if checkbox_name in request.POST:
                selected_checkboxes.append(checkbox_name)
        
        # Perform any additional processing with the selected checkboxes
        recipes = []
        for x in col2.find({'Ingredients':{'$all':selected_checkboxes}}):
            recipes.append(x['Recipe'])
        #recipetext = " " #recipe should be in this variable
        #new_recipetext = recipetext.replace('Step', '\nStep')
 
        context = {
            'selected_checkboxes': selected_checkboxes,
            'recipes' : recipes
        }
        return render(request, 'result.html', context)
    
    return render(request, 'test.html')
