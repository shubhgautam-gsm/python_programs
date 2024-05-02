import mysql.connector

try:
    # create connection and cursor objects
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="py1121")
    cursor = connection.cursor()

    # build a query
    query = "SELECT * FROM students"

    # execute query
    cursor.execute(query)

    # fetch all rows and store them in a list
    all_rows = cursor.fetchall()

    # if there are rows fetched, print the last row
    if all_rows:
        last_row = all_rows[5]  # Get the last row from the fetched results
        print(last_row)
    else:
        print("No rows found in the 'students' table")

    connection.commit()
    connection.close()
    
except Exception as err:
    connection.rollback()
    print("Error is ",err)
