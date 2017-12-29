from django.shortcuts import render, get_object_or_404, redirect
from .models import Resident, Goal, Progress
from .forms import GoalForm, ResidentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'zoom_data/home.html')

@login_required(login_url='/login/')
def resident_list(request):
	residents = Resident.objects.filter(resident_exit__isnull = True).order_by('resident_last_name')
	return render(request, 'zoom_data/resident_list.html', {'residents' : residents})

@login_required(login_url='/login/')
def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request, 'zoom_data/resident_detail.html', {'resident': resident})

@login_required(login_url='/login/')
def goal_new(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.save()
            return redirect('resident_list')
    else:
        form = GoalForm()
    return render(request, 'zoom_data/goal_edit.html', {'form': form})

@login_required(login_url='/login/')
def resident_new(request):
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.save()
            return redirect('resident_list')
    else:
        form = ResidentForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/resident_edit.html', {'form': form})

@login_required(login_url='/login/')
def activity_follow_up(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request, 'zoom_data/resident_detail.html', {'resident': resident})