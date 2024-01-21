from django.shortcuts import render
from .models import *

def home(request):
    context = {
        'models': ['UserProfile', 'Calendar', 'Event', 'Task', 'Diary']
    }
    return render(request, 'home.html', context)
