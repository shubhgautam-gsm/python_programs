import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="",
    database="py1121")

    myCursor = connection.cursor()
    query = "create table students (id INT AUTO_INCREMENT PRIMARY KEY,fname VARCHAR(255),lname VARCHAR(255),\
    city VARCHAR(255),email VARCHAR(255),phone VARCHAR(255),gender ENUM('male', 'Female')"
    result = myCursor.execute(query)
    print("Table Created")

    connection.close()
except Exception as err:
    print("Error is ",err)