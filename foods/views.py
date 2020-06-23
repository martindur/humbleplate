from django.shortcuts import render

# Create your views here.
from .models import Food

def frontend(request):
    """ Vue.js """

    foods = Food.objects.all()

    data = {'foods': foods}

    return render(request, 'foods/template.html', data)