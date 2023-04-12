# 4.	Напишіть програму, яка змінює у таблиці 'student' поле 'id' на PRIMARY KEY.

import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gamalya180675",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE student modify id INT AUTO_INCREMENT PRIMARY KEY")
