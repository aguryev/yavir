from main.models import KeyPerson
from django.contrib.auth.models import Group

persons = [
	[
		'Головний вчитель',
		'Леся Музика',
		'066 654 71 70',
		],
	[
		'Вчитель англійської мови та музики',
		'Ольга Орленко',
		'067 731 04 51',
		],
	[
		'Другий вчитель',
		'Наталія Ковальова',
		'097 115 25 10',
		],
	[
		'Корекційний педагог',
		'Анастасія Пасєчнік',
		'095 579 04 32',
		],
	[
		'Вчитель групи подовженого дня',
		'Роман Свідерський',
		'093 580 42 47',
		],
	[
		'Вчитель німецької мови',
		'Верена Йеггле',
		'099 058 73 33',
		],
	[
		'Вчитель евритмії',
		'Ірина Токова',
		'063 771 88 27',
		],
	[
		'Акомпаніатор',
		'Сергій Копил',
		'',
		],
	[
		'Координатор класу',
		'Марина Мариняк',
		'0667116006',
		],
	]

group = Group.objects.get(name='class_3')
for p in persons:
	name = p[1].split()
	tel = '+38' + ''.join(p[2].split())
	person = KeyPerson(
		first_name=name[0],
		last_name=name[1],
		description=p[0],
		phone_number=tel,
		group=group,
		)
	person.save()
	
	print(person)




