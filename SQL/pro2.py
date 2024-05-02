import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="")
    print("Database Connected")
    myCursor = connection.cursor()
    query = "create database students"
    result = myCursor.execute(query)
    print("Database Created students")

    connection.close()
except Exception as err:
    print("Error is ",err)