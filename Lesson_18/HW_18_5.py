# 5.	Напишіть програму, яка додає до таблиці 'student' дані (01, 'John’), '
# а до таблиці 'employee' - (01, ’John', 10000)

import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gamalya180675",
    database="my_first_db"
)

# Insert Into Table student
mycursor = mydb.cursor()
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = (1, "John")
mycursor.execute(sql, val)
mydb.commit()

# Insert Into Table employee
mycursor = mydb.cursor()
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = (1, "John", 10000)
mycursor.execute(sql, val)
mydb.commit()
