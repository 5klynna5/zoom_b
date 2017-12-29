from django.shortcuts import render, redirect, get_object_or_404
from .models import Volunteer, Activity, Hours
from .forms import HoursForm, VolunteerForm

def volunteer_home(request):
	return render(request, 'zoom_vols/volunteer_home.html')

def volunteer_list(request):
	volunteers = Volunteer.objects.all()
	return render(request, 'zoom_vols/volunteer_list.html', {'volunteers' : volunteers})

def volunteer_detail(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    return render(request, 'zoom_vols/volunteer_detail.html', {'volunteer': volunteer})


def hours_new(request):
    if request.method == "POST":
        form = HoursForm(request.POST)
        if form.is_valid():
            hours = form.save(commit=False)
            hours.save()
            return redirect('volunteer_list')
    else:
        form = HoursForm()
    return render(request, 'zoom_vols/hours_new.html', {'form': form})

def volunteer_new(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'zoom_vols/volunteer_new.html', {'form': form})

