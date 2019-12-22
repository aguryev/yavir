from main.models import Lesson
from datetime import datetime, time
from django.contrib.auth.models import Group

lessons = [
	[
		'Епохальний урок',
		'Музика',
		'Німецька',
		'Ліплення',
		],
	[
		'Епохальний урок',
		'Німецька',
		'Живопис',
		'Рукоділля',
		],
	[
		'Епохальний урок',
		'Німецька',
		'Читання',
		'Рухливі ігри',
		],
	[
		'Епохальний урок',
		'Англійська',
		'Рукоділля / Евритмія',
		'Евритмія / Рукоділля',
		],
	[
		'Епохальний урок',
		'Англійська',
		'Музика',
		'Читання (додатковий)',
		'Рухливі ігри',
		],
	]

times = [
	('08:30', '10:10'),
	('10:25', '11:10'),
	('11:30', '12:15'),
	('12:35', '13:20'),
	('13:30', '14:15'),
	]

day_counter = 0
group = Group.objects.get(name='class_3')
for day in lessons:
	lesson_index = 0
	start_day = 23 # 23-09-2019
	for lesson in day:
		start_time = datetime.strptime(str(start_day + day_counter) + '-09-2019 ' + times[lesson_index][0], '%d-%m-%Y %H:%M')
		end_time = datetime.strptime(times[lesson_index][1], '%H:%M')
		lesson_obj = Lesson(
			title=lesson,
			start_time=start_time,
			end_time=end_time,
			group=group,
			)
		print(lesson_obj)
		lesson_obj.save()

		lesson_index += 1
	day_counter += 1




