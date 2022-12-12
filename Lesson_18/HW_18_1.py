# 1.	Напишіть програму, яка створює нову базу даних 'my_first_db'.
import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gamalya180675",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
