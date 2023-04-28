from django.shortcuts import render

def index(request):
    print('HELLLLLLLLLLLLLLLLLLLLLLLLLLLO')
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        print(request.POST)
        selected_checkboxes = []
        checkbox_names = ['potato', 'cauli', 'onion']
        for checkbox_name in checkbox_names:
            if checkbox_name in request.POST:
                selected_checkboxes.append(checkbox_name)
        
        # Perform any additional processing with the selected checkboxes
        
        context = {
            'selected_checkboxes': selected_checkboxes
        }
        
        return render(request, 'result.html', context)
    
    return render(request, 'test.html')
