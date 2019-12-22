from main import models

contacts = (
	('4 клас', 'Аліна', '(050) 717 7787'),
	('5 клас', 'Ірина', '(095) 792 8665')
	)


for c in contacts:
	c_object = models.ContactPerson(
		name=c[1],
		phone=c[2],
		brief=c[0],
		)
	print(c_object)
	c_object.save()
