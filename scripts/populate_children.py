from main.models import Child, Class
from datetime import date
import json

def get_date(dt):
	try:
		date_list = dt.split('.')
		d = date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
		return d
	except:
		return None

json_children = 'scripts/children.json'

# load children
with open(json_children, 'r') as f:
	children = json.load(f)

# get or create class
clss, created = Class.objects.get_or_create(
	title='3-B',
	start_year=2017,
	)

# loop children
for ch in children:
	Child.objects.get_or_create(
		first_name=ch['first_name'],
		last_name=ch['last_name'],
		birthday=get_date(ch['birthday']),
		class_id=clss,  
		)
