from django.contrib import admin

from .models import Resident, Goal, Progress

admin.site.register(Resident)
admin.site.register(Goal)
admin.site.register(Progress)
