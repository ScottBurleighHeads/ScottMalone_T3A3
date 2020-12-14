import psycopg2
import os
connect = psycopg2.connect (
    dbname= 't3a3', 
    user= 'scott', 
    password= os.getenv("DB_PASSWORD"), 
    host= 'localhost')  # Needed to create role first when creating database.

cursor = connect.cursor()
cursor.execute("SELECT * FROM student;")
cursor.fetchall()
connect.commit()
cursor.close()
connect.close()