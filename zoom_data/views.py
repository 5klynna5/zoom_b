from django.shortcuts import render
from .models import Resident, Goal, Progress

def resident_list(request):
    return render(request, 'zoom_data/resident_list.html')
