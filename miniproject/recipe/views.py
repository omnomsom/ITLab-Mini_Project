from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        print(request.POST)
        selected_checkboxes = []
        checkbox_names = ['Potato', 'Cabbage', 'Onions', 'Tomato', 'French Beans', 'Beetroot', 'Garlic', 'Rice', 'Paneer', 'Curd', 'Chicken', 'Green Chillies', 'Cream', 'Butter', 'Fruits', 'Capsicum', 'Bread', 'Lemon', 'Maida', 'Cheese']
        for checkbox_name in checkbox_names:
            if checkbox_name in request.POST:
                selected_checkboxes.append(checkbox_name)
        
        # Perform any additional processing with the selected checkboxes
       
        recipetext = " " #recipe should be in this variable
        new_recipetext = recipetext.replace('Step', '\nStep')
 
        context = {
            'selected_checkboxes': selected_checkboxes,
            'recipetext':new_recipetext
        }
        return render(request, 'result.html', context)
    
    return render(request, 'test.html')
