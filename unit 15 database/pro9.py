import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="py1121")
    connection.autocommit = True
    myCursor = connection.cursor()

    query = "INSERT INTO students (id, fname, lname, city, email, phone, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    data = [
        (12, "Nikitavs", "Rathod", "Rajkot", "Priya@atmiyauni.edu", "9988998899", "Female"),
        (13, "Bita", "Rathod", "Rajkot", "Priya@atmiyauni.edu", "9988998899", "Female")
    ]

    myCursor.executemany(query, data)
    print(myCursor.rowcount, "New Record(s) Created")

    # Retrieve the last inserted row ID (lastrowid)
    last_row_id = myCursor.lastrowid
    if last_row_id is not None:
        print("Last Inserted Row ID:", last_row_id)

    connection.commit()
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
