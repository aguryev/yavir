from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group
#from django.contrib.auth.models import User, Group
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.

# site sections 
SECTION_HOME = 0
SECTION_CLASS = 1

# article status
STATUS_UNPUBLISHED = 0
STATUS_PUBLISHED = 1
STATUS_DECLINED = 2

class Class(models.Model):
	#
	# object of a class
	#
	title = models.CharField(max_length=16)
	start_year = models.IntegerField(default=timezone.now().year)

	class Meta:
		verbose_name_plural = 'classes'

	def __str__(self):
		return self.title


class Child(models.Model):
	#
	# object of a child
	#
	first_name = models.CharField(max_length=16)
	last_name = models.CharField(max_length=16)
	birthday = models.DateField(blank=True, null=True)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'children'

	def __str__(self):
		return f'{self.last_name} {self.first_name}'

# -------> START: custom user  definition
class UserManager(BaseUserManager):
	
	def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError('Email is mandatory')
		email = self.normalize_email(email)
		user = self.model(
			email=email,
			is_staff=is_staff,
			is_superuser=is_superuser,
			**extra_fields,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password, **extra_fields):
		return self._create_user(email, password, False, False, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		user = self._create_user(email, password, True, True, **extra_fields)
		user.save(using=self._db)
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=64, unique=True)
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	last_login = models.DateTimeField(null=True, blank=True)
	date_joined = models.DateTimeField(default=timezone.now)
	children = models.ManyToManyField(Child)

	USERNAME_FIELD = 'email'
	ENAIL_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	def get_absolute_url(self):
		return "/users/{self.id}/"

# -------> END: custom user  definition

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
		(SECTION_HOME, 'home'),
		(SECTION_CLASS, 'class'),
		))
	position = models.IntegerField(default=0)
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
		(STATUS_UNPUBLISHED, 'Unpublished'),
		(STATUS_PUBLISHED, 'Published'),
		(STATUS_DECLINED, 'Declined'),
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


	
