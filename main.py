import psycopg2

connect = psycopg2.connect (dbname= 't3a3', user= 'scott', password= 'easypassword', host= 'localhost')

cursor = connect.cursor()
cursor.execute("CREATE TABLE student(id SERIAL PRIMARY KEY,name VARCHAR);")
connect.commit()
cursor.close()
connect.close()
