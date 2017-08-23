from django.db import models
from radio.profiles.models import Staff
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

class Day(models.Model):
	DAY_CHOICES = (('MON','MONDAY'),('TUE','TUESDAY'),('WED','WEDSDAY'),
					('THU','THURSDAY'),('FRI','FRIDAY'),('SAT','SATURDAY'),
	               ('SUN','SUNDAY'))
	name = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True)

	def get_absolute_url(self):
		return reverse('program:day_detail', kwargs={'day':self.name})

	def __str__(self):
		return self.name


class Time(models.Model):
	start = models.TimeField(null=True, blank=True)
	duration= models.DurationField(null=True, blank=True)
	end = models.TimeField(null=True, blank=True)
	day = models.ManyToManyField(Day)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	program = models.ForeignKey('Program', null=True, blank=True)

	def __str__(self):
		return ('From %r to %r ' % (self.start, self.end))


class Program(models.Model):
	title = models.CharField(max_length=250, unique=True)
	description = models.TextField(default='')
	presenters = models.ManyToManyField(Staff)
	slug = models.SlugField(editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
		if not self.slug:
			self.slug = slugify(self.title)
		return super(Program, self).save()


	def get_absolute_url(self):
		return reverse('program:program_detail', kwargs={'slug': self.slug})


	def __str__(self):
		return self.title

class Event(models.Model):
	date = models.DateTimeField(null=True, blank=True)
	title = models.CharField(max_length=250, unique_for_month=True)
	description = models.TextField(default='')
	presenters = models.ManyToManyField(Staff)
	slug = models.SlugField(editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super(Event, self).save()


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('program:event_detail', kwargs={'slug': self.slug})


from django.db import models
from django.contrib import admin

class Person(models.Model):
    name = models.CharField(max_length=128)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
