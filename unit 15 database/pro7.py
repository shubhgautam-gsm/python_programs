import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="",
    database="py1121")

    myCursor = connection.cursor()
    query = "insert into students (fname, lname, city, email, phone, gender) values (" \
            "%s, %s, %s, %s, %s, %s)"
    data = ("Priya", "Rathod", "Rajkot", "Priya@atmiyauni.edu", "9988998899", "Female")
    myCursor.execute(query, data)
    data2 = ("jay", "gondaliya", "Surat", "jay@atmiyauni.edu", "9955998899", "male")
    myCursor.execute(query, data2)
    print("New Record Inserted")
    connection.commit()
    connection.close()
except Exception as err:
    connection.rollback()
    print("Error is ",err)