from django import forms

from .models import Hours, Volunteer, Activity

class HoursForm(forms.ModelForm):

    class Meta:
        model = Hours
        fields = ('volunteer', 'volunteer_activity', 'date', 'hours_num')

class VolunteerForm(forms.ModelForm):
    
    class Meta:
        model = Volunteer
        exclude = ['volunteer_id', 'date_updated']
