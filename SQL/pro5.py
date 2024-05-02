import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="",
    database="students")

    myCursor = connection.cursor()
    query = "create table marks (marksid int auto_increment primary key, roll int," \
            " total int, result varchar(20))"
    result = myCursor.execute(query)
    print("Table Created")
    print(result)
    connection.close()
except Exception as err:
    print("Error is ",err)