import sqlite3
import re

pre_filename = 'copy.db.sqlite3'
sql_filename = 'db.sqlite3'

# connect previous DB
conn_pre = sqlite3.connect(pre_filename)
pre  = conn_pre.cursor()
# get table list
query = "SELECT name FROM sqlite_master WHERE type = 'table'"
pre.execute(query)
table_list = [table[0] for table in pre.fetchall() if re.match(r'main_', table[0])]

print(table_list)

# connect new DB
conn_new = sqlite3.connect(sql_filename)
sql = conn_new.cursor()

# copy data
for table in table_list:
	print(f'table: {table}')
	# get sql columns
	query = f"SELECT * from {table} where 1=0"
	pre.execute(query)
	sql_col = [name[0] for name in pre.description]
	for i in range(len(sql_col)):
		if sql_col[i] == 'index':
			sql_col[i] = 'position'
	print(sql_col)

	# get sql data
	query = f"SELECT * FROM {table}"
	pre.execute(query)

	# add data to new DB
	for data in pre.fetchall():
		# update author_ids with 1
		for i in range(len(sql_col)):
			if sql_col[i] == 'author_id':
				data[i] == 1

		print (f'data: {data[0]}')
		query = ''.join((
			f"INSERT INTO {table}(",
			','.join(sql_col),
			') VALUES(',
			','.join(["?" for i in range(len(sql_col))]),
			')',
			))
		#for i in range(len(data)):
		#	print(f"{sql_col[i]}: '{data[i]}' - '{data_update[i]}'")
		#print(query)
		#print(data)

		sql.execute(query, data)

# save changes
conn_new.commit()

# close connections
conn_new.close()
conn_pre.close()

