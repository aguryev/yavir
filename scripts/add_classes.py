from main import models
#import sqlite3

db_filename = 'db.sqlite3'

titles = (
	'1-й клас',
	'2-й клас',
	'3-й клас',
	'4-й клас',
	'5-й клас',
	)

imgs = (
	'class_1.jpg',
	'class_2.jpg',
	'class_3.jpg',
	'class_4.jpg',
	'class_5.jpg',
	)

briefs = (
	"Програма першого класу передбачає мистецтво, музику, садівництво, дітей знайомлять з буквами",
	"Що вивчають діти? Звичайні предмети (письмо, математика, читання) викладаються враховуючи",
	"Лейтмотивом третього класу вальдорфської школи є перші кроки дитини у самостійне життя",
	"10 років – успішно пройдений перехід від дитячої наївності до власного ставлення до всього в світі",
	"П'ятий клас — цікавий вік у житті дитини. Що відбувається в школі у цей період? Перша підліткова криза",
	)

description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

"""
# connect DB
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
#query = 'SELECT name FROM sqlite_master where type="table"'
query = 'SELECT * FROM "main_classdescription"'
cursor.execute(query)

for table in cursor.description:
	print(table)

"""
for i in range(len(titles)):
	class_object = models.ClassDescription(
		title=titles[i],
		img_url=imgs[i],
		brief=briefs[i],
		description=description,
		)
	print(class_object)
	class_object.save()
