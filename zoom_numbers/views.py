from django.shortcuts import render, get_object_or_404, redirect
from .models import YMCA, FoodShelf

def ymca_visits(request):
	visits = YMCA.objects.all()
	return render(request, 'zoom_data/ymca_visits.html', {'visits': visits})
