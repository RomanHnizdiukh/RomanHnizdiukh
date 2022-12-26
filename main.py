import mysql.connector
mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = "Rombig8098",
    port='3306',
    database = 'mavenmovies',
)
cursor = mydb.cursor()

cursor.execute("""UPDATE actor SET first_name="ROMAN" WHERE actor_id=192""")

cursor.execute("""SELECT * FROM actor WHERE actor_id=192 """)

for actor in cursor:
   print(actor)

mydb.commit()
