from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def people(request):
    
    people = [
        {
            'id': 1,
            'name': 'Bob Smith',
            'age': 35,
            'country': 'USA'
        },
        {
            'id': 2,
            'name': 'Martha Smith',
            'age': 60,
            'country': 'USA'
        },
        {
            'id': 3,
            'name': 'Fabio Alberto',
            'age': 18,
            'country': 'Italy'
        },
        {
            'id': 4,
            'name': 'Dietrich Stein',
            'age': 85,
            'country': 'Germany'
        }
    ]

    context = {
        'all_people': people 
    }

    html_page = render(request, 'people.html', context)

    return html_page

def people_id(request)
