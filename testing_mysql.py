import mysql.connector

mydb = mysql.connector.connect(host="localhost",user='root',passwd="Akanksha@141")
print(mydb.connection_id)
print("mysql.connector connected successfully")
