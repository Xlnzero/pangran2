from django.shortcuts import render

def index(request):
    date = {
        'title': 'Главная страница!!!',
        'values': ['Some','Hello','123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'


        }
    }
    return render(request, 'main/index.html', date)

def about(request):
    return render(request, 'main/about.html')