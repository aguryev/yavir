import psycopg2

db_url = 'postgres://ocidbmxfzmcauw:bf89ba679538c04f4892a95e6d01f4086455c2c5d02f91dc445006fff370c595@ec2-174-129-24-148.compute-1.amazonaws.com:5432/dcs49j7lqp5kbf'

# connect DB
conn = psycopg2.connect(db_url)
cursor = conn.cursor()
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
#query = 'SELECT * FROM "main_classdescription"'
cursor.execute(query)

for table in cursor.fetchall():
	print(table)


