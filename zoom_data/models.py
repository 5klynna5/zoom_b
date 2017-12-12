from django.db import models
from django.utils import timezone

class Resident(models.Model):
	resident_id = models.AutoField(primary_key=True)
	resident_first_name = models.CharField(max_length=20)
	resident_last_name = models.CharField(max_length=20)
	resident_move_in = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	
	INSURANCE_CHOICES = (
		('NONE', 'None'),
		('PRIVATE', 'Private'),
		('MEDICAID', 'Medicaid'),
		('OTHER', 'Other Insurance'),
	)

	health_ins = models.CharField(max_length = 8, choices=INSURANCE_CHOICES, blank=True, null=True)
	unit_num = models.PositiveSmallIntegerField(blank=True, null=True)

	UNIT_CHOICES = (
		('Supportive Housing', 'SUPPORTIVE'),
		('MARIF', 'MARIF'),
		('Studio', 'STUDIO'),
	)

	unit_type = models.CharField(max_length = 10, choices=UNIT_CHOICES, blank=True, null=True)
	resident_exit  = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", null=True, blank=True)

	@property
	def goals(self):
		return self.goal_set.all()

	@property
	def phone(self):
		if self.contact_set.all().order_by('-id').first() is None:
			return "None"
		else:
			return self.contact_set.all().order_by('-id').first().resident_phone
	
	@property
	def email(self):
		if self.contact_set.all().order_by('-id').first() is None:
			return "None"
		else:
			return self.contact_set.all().order_by('-date_updated').first().resident_email

	@property
	def contact_preferred(self):
		if self.contact_set.all().order_by('-id').first() is None:
			return "None"
		else:
			return self.contact_set.all().order_by('-date_updated').first().contact_pref

	def __str__(self):
		return (self.resident_last_name) + ', ' + (self.resident_first_name)

	@property
	def activities(self):
		return self.attendance_set.all()



class Contact(models.Model):
	contact_resident = models.ForeignKey('Resident')
	resident_phone = models.CharField( max_length=10, blank=True, null=True)
	resident_email = models.EmailField(blank=True, null=True)

	PERMISSION_CHOICES = {
		('Yes', 'YES'),
		('No', 'NO'),
	}
	permission_text = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_photo = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_email = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_call = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_mail = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_facebook = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)

	CONTACT_CHOICES = {
		('Text', 'TEXT'),
		('Call', 'CALL'),
		('Email', 'EMAIL'),
		('Mail', 'MAIL'),
		('Facebook', 'FACEBOOK')
	}

	contact_pref = models.CharField(max_length=8, choices=CONTACT_CHOICES, blank=True, null=True)

	date_updated = models.DateTimeField(blank=True, null=True)
	
	def update(self):
		self.date_updated = timezone.now()
		self.save()
	
	def __str__(self):
		return str(self.contact_resident) + ' ' + str(self.date_updated.strftime("%m-%d-%Y"))

class Goal(models.Model):
	goal_name = models.CharField(max_length = 100)
	goal_date = models.DateField(blank=True, null=True)
	goal_explain = models.TextField(blank=True)
	goal_resident = models.ForeignKey('Resident')

	@property
	def current_progress(self):
		if self.progress_set.all().order_by('-id').first() is None:
			return "less than 25%"
		else:
			return self.progress_set.all().order_by('-id').first().percent_progress

	def __str__(self):
		return str(self.goal_date)+" : "+ str(self.goal_name)


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
	percent_progress = models.CharField(max_length=13, choices=PROGRESS_CHOICES, blank=True, default = "less than 25%")
	notes_progress = models.TextField(blank=True)

	def __str__(self):
		return str(self.goal) + " " + str(self.date_progress)

class Activity(models.Model):
	activity_name = models.CharField(max_length=25)
	
	SKILL_CHOICES = (
		('FINANCE', 'Finance'),
		('PARENTING', 'Parenting'),
		('EMPLOYMENT', 'Employment'),
	)

	skill_area = models.CharField(max_length = 15, choices=SKILL_CHOICES, blank=True, null=True)
	members = models.ManyToManyField(Resident, through='Attendance')

	def __str__(self):
		return str(self.activity_name)


class Attendance(models.Model):
	resident = models.ForeignKey(Resident)
	activity = models.ForeignKey(Activity)
	complete_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return str(self.activity)

