import re
import json

input_file = 'children.txt'
json_out = 'children.json'

def read_file(filename):
	with open(filename, 'r') as f:
		while True:
			line = f.readline()
			if line:
				yield line
			else:
				break

def person_as_dict(person):
	print(person)
	if person[1] is None:
		return {
			'first_name': person[0],
			'last_name': None,
			'phone': person[3],
			}
	else:
		return {
			'first_name': person[1].strip(),
			'last_name': person[0],
			'phone': person[3],
			}



def parse_line(line):
	data = {}
	# get name
	name = re.match(r'\d+\s+([\w\']+)\s+(\w+)', line)
	if name:
		data['first_name'] = name.group(2)
		data['last_name'] = name.group(1)
	# get birthday
	birthday = re.search(r'\((\d{2}\.\d{2}\.\d{4})\)', line)
	if birthday:
		data['birthday'] = birthday.group(1)
	else:
		data['birthday'] = None

	# get mother
	mother = re.search(r'мама\s+([\w\']+)(\s+\w+)?(\s+\((\+\d{7,})\))?', line)
	if mother:
		data['mother'] = person_as_dict(mother.groups())
	else:
		data['mother'] = {
			'first_name': None,
			'last_name': None,
			'phone': None,
			}

	# get father		
	father = re.search(r'тато\s+([\w\']+)(\s+\w+)?(\s+\((\+\d{7,})\))?', line)
	if father:
		data['father'] = person_as_dict(father.groups())
	else:
		data['father'] = {
			'first_name': None,
			'last_name': None,
			'phone': None,
			}
	return data

children = []
for line in read_file(input_file):
	children.append(parse_line(line))

with open(json_out, 'w') as f:
	json.dump(children, f)


