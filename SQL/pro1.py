import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="")
    print("Database Connected")
    connection.close()
except Exception as err:
    print("Error is ",err)