from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.

class SiteArticle(models.Model):
	#
	# site article object
	#
	title = models.CharField(max_length=50)
	brief = models.CharField(max_length=100, blank=True)
	text = HTMLField() # reach text tinymce field
	image = models.ImageField(blank=True) 
	changed = models.DateTimeField(default=timezone.now)
	# article section
	section = models.IntegerField(choices=(
		(0, 'home'),
		(1, 'class'),
		))
	index = models.IntegerField(default=0)
	is_active = models.BooleanField(default=True)


	def __str__(self):
		return self.title

class BlogArticle(models.Model):
	#
	# blog article object
	#
	title = models.CharField(max_length=50)
	brief = models.CharField(max_length=300)
	text = HTMLField() # reach text tinymce field 
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	posted = models.DateTimeField(default=timezone.now)
	# status of the article
	status = models.IntegerField(default=0, choices=(
		(0, 'Unpublished'),
		(1, 'Published'),
		(2, 'Declined'),
		))

	def __str__(self):
		return ' '.join((
			self.posted.strftime('%d-%m-%Y'),
			self.title,
			))

class ArticleComment(models.Model):
	#
	# comment to a blog article
	#
	text = HTMLField() # reach text tinymce field 
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	posted = models.DateTimeField(default=timezone.now)
	article = models.ForeignKey(BlogArticle, on_delete=models.CASCADE)

	def __str__(self):
		return ' '.join((
			self.posted.strftime('%d-%m-%Y %H:%m'),
			self.article.title,
			))

class Event(models.Model):
	#
	# event object
	#
	title = models.CharField(max_length=100)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	image = models.ImageField()
	description = HTMLField() # reach text tinymce field 
	time_start = models.DateTimeField(default=timezone.now)
	time_end = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return ' '.join((
			self.group.name,
			self.time_start.strftime('%d-%m-%Y'),
			self.title,
			))

class EventComment(models.Model):
	#
	# comment to an event
	#
	text = HTMLField() # reach text tinymce field 
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	posted = models.DateTimeField(default=timezone.now)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

	def __str__(self):
		return ' '.join((
			self.posted.strftime('%d-%m-%Y %H:%m'),
			self.event.title,
			))

class Lesson(models.Model):
	title = models.CharField(max_length=32)
	start_time = models.DateTimeField()
	end_time = models.TimeField()
	group = models.ForeignKey(Group, on_delete=models.CASCADE) 

	def __str__(self):
		return self.start_time.strftime('%A %H:%M')

	def get_time_span(self):
		return ' - '.join([self.start_time.strftime('%H:%M'), self.end_time.strftime('%H:%M')])

	def get_day_int(self):
		return int(self.start_time.strftime('%w'))

class KeyPerson(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	description = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=13)
	is_active = models.BooleanField(default=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

	def __str__(self):
		return ' '.join((self.first_name, self.last_name))


	
