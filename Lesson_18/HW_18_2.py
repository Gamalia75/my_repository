# 2.	Напишіть програму, яка створить у базі 'my_first_db', таблицю 'student',
# з полями 'id' (INT) і 'name' (VARCHAR(255)).

import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gamalya180675",
    database="my_first_db"
)

# Creating a Table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
