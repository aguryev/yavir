from django.contrib.auth.models import Group

# define list of the users groups
CLASS_GROUPS = {
	'class_1': '1-й клас',
	'class_2': '2-й клас',
	'class_3': '3-й клас',
	'class_4': '4-й клас',
	}

ACTIVE_GROUPS = [
	'pr',
	'it',
	'finance',
	]

def create_groups(sender, **kwargs):
	#
	# create user groups
	#
	# default group
	group_app, created = Group.objects.get_or_create(name='default')
	# class groups
	for group in CLASS_GROUPS:
		group_app, created = Group.objects.get_or_create(name=group)
	# active groups
	for group in ACTIVE_GROUPS:
		group_app, created = Group.objects.get_or_create(name=group)