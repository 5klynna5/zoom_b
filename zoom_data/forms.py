from django import forms
from .models import Resident, Goal, Progress
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget 
from functools import partial
from datetime import datetime
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ('goal_name', 'goal_date', 'goal_explain', 'goal_resident')

class ResidentForm(forms.ModelForm):

	class Meta:
		model = Resident
		fields = ('resident_first_name', 'resident_last_name', 'resident_move_in')
		widgets = {'resident_move_in': DateInput()}
       