# 3.	Напишіть програму, яка створить у базі 'my_first_db', таблицю 'employee',
# з полями 'id' (INT AUTO_INCREMENT PRIMARY KEY), 'name' (VARCHAR(255)) і 'salary' (INT(6))

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
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
