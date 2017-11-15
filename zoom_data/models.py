from django.db import models
from django.utils import timezone

class Resident(models.Model):
	resident_id = models.AutoField(primary_key=True)
	resident_first_name = models.CharField(max_length=20)
	resident_last_name = models.CharField(max_length=20)
	resident_move_in = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	resident_exit  = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", null=True, blank=True)

	def __str__(self):
		return (self.resident_last_name) + ', ' + (self.resident_first_name)


class Goal(models.Model):
	goal_name = models.CharField(max_length = 100)
	goal_date = models.DateField(blank=True, null=True)
	###this is messing up the migration and cannot get it to fix
	goal_explain = models.TextField(blank=True)
	goal_resident = models.ForeignKey('Resident')

	def __str__(self):
		return str(self.goal_resident)+" : "+ str(self.goal_name)


class Progress(models.Model):

	PROGRESS_CHOICES = (
		('less than 25%', 'less than 25%'),
		('25%', '25%'),
		('50%', '50%'),
		('75%', '75%'),
		('100%', '100%'),
	)

	goal = models.ForeignKey('Goal')
	date_progress = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	percent_progress = models.CharField(max_length=13, choices=PROGRESS_CHOICES, blank=True)
	notes_progress = models.TextField(blank=True)

	def __str__(self):
		return str(self.goal) + " " + str(self.date_progress)

