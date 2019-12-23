import psycopg2
import sqlite3
import re

pg_url = 'postgres://ocidbmxfzmcauw:bf89ba679538c04f4892a95e6d01f4086455c2c5d02f91dc445006fff370c595@ec2-174-129-24-148.compute-1.amazonaws.com:5432/dcs49j7lqp5kbf'
sql_filename = 'db.sqlite3'

# connect PG
conn = psycopg2.connect(pg_url)
pg = conn.cursor()

# get tables
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
pg.execute(query)
table_list = [table[0] for table in pg.fetchall() if re.match(r'main_', table[0])]

# connect SQLite
conn_sql = sqlite3.connect(sql_filename)
sql = conn_sql.cursor()

# copy data
for table in table_list[1:6]:
	print(f'table: {table}')
	# get sql columns
	query = f"SELECT * from {table} where 1=0"
	sql.execute(query)
	sql_col = [name[0] for name in sql.description]

	# get sql data
	query = f"SELECT * FROM {table}"
	sql.execute(query)

	# add data to PG
	for data in sql.fetchall():
		# replace booleans
		data_update = []
		for i in range(len(sql_col)):
			if re.match(r'is_', sql_col[i]):
				data_update.append(data[i] == 1)
			else:
				data_update.append(data[i])

		print (f'data: {data[0]}')
		query = ''.join((
			f"INSERT INTO {table}(",
			','.join(sql_col),
			') VALUES(',
			','.join(["%s" for i in range(len(sql_col))]),
			')',
			))
		pg.execute(query, data_update)

# save changes
conn.commit()

# close connections
conn.close()
conn_sql.close()

