from django import template
#from django.contrib.auth.models import User
from ..models import User
from django.utils import timezone
from .. import signals

register = template.Library()

WEEKDAYS = [
	"Понеділок",
	"Вівторок",
	"Середа",
	"Четвер",
	"П'ятниця",
	"Субота",
	"Неділя",
	]

MONTHES = [
	'Січня',
	'Лютого',
	'Березня',
	'Квітня',
	'Травня',
	'Червня',
	'Липня',
	'Серпня',
	'Вересня',
	'Жовтня',
	'Листопада',
	'Грудня',
	]

DAYS = [
	'Сьогодні',
	'Вчора',
	]

@register.simple_tag
def admin_email():
	#
	# returns admin's email
	#
	try:
		admin = User.objects.get(id=1)
		return admin.email
	except User.DoesNotExist:
		return ''

@ register.simple_tag
def user_name(user):
	#
	# get formatted user's name
	# 
	if user.first_name or user.last_name:
		return f'{user.first_name} {user.last_name}'.strip()
	else:
		return user.email.split('@')[0].capitalize()

@register.simple_tag
def group_list(group_type):
	#
	# get list of groups of the specific type:
	#

	if group_type == 'class':
		return signals.CLASS_GROUPS
	elif group_type == 'active':
		return signals.ACTIVE_GROUPS
	else:
		return []

@register.simple_tag
def today(format):
	#
	# get formatted today date
	#
	
	now = timezone.now()
	if format == 'weekday':
		return WEEKDAYS[now.weekday()]
	elif format == 'date':
		return f'{now.day}.{now.month}.{now.year}'
	else:
		return 'NOT DEFINED'

@register.filter('in_group')
def in_group(user, group_name):
	#
	# check if the user is in the group 'group_name'
	#
	return user.groups.filter(name=group_name).exists()

@register.filter('format_date')
def format_date(date, option):
	#
	# formats date as option:
	# date -> day.month.year_if_not_current
	# full -> (day.month)_if_not_today.year_if_not_current hours:minutes
	#
	now = timezone.now()
	result = ''
	# date option
	if now.year == date.year and now.month == date.month and now.day == date.day:
		result = DAYS[0]
	elif now.year == date.year and now.month == date.month and now.day == (date.day + 1):
		result = DAYS[1]
	else:
		result = f'{date.day} {MONTHES[date.month-1]}'
		if now.year != date.year:
			result += f' {date.year}'

	# full option
	if option == 'full':
		result += f', {date.hour:0=2d}:{date.minute:0=2d}'

	return result


@register.filter('get_date')
def get_date(date):
	#
	# format date
	#
	
	if timezone.now().year == date.year:
		return f'{date.day} {MONTHES[date.month-1]}'
	else:
		return f'{date.day} {MONTHES[date.month-1]} {date.year}'

@register.filter('get_header')
def get_header(tab):
	if tab == '0':
		return 'Час'
	else:
		return WEEKDAYS[int(tab) - 1]

@register.filter('is_today')
def is_today(day):
	return (int(day) - 1) == timezone.now().weekday()

@register.filter('get_phone')
def get_phone(phone_number):
	#
	# format phone number
	#
	return ' '.join((
			phone_number[:4],
			phone_number[4:6],
			phone_number[6:9],
			phone_number[9:11],
			phone_number[11:],
			))