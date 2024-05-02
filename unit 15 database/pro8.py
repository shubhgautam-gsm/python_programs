import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="py1121")
    cursor = connection.cursor()

    query = "INSERT INTO students (id, fname, lname, city, email, phone, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    data = [
        (1, "Priya", "Rathod", "Rajkot", "Priya@atmiyauni.edu", "9988998899", "Female"),
        (2, "Ashita", "Gohel", "Rajkot", "aashita@atmiyauni.edu", "9988998899", "Female"),
        (3, "Naisargi", "Sondagar", "Rajkot", "Naisargi@atmiyauni.edu", "9988998899", "Female"),
        (4, "Ganga", "Khatri", "Rajkot", "Ganga@atmiyauni.edu", "9988998899", "Female"),
        (5, "Jigar", "Vaghela", "Rajkot", "Jigar@atmiyauni.edu", "9988998899", "Male"),
        (6, "Sunny", "Sata", "Rajkot", "sunny@atmiyauni.edu", "9988998899", "Male"),
        (7, "Kalpesh", "Kisla", "Rajkot", "kalpesh@atmiyauni.edu", "9988998899", "Male"),
        (8, "Nikhil", "DObariya", "Rajkot", "nikhil@atmiyauni.edu", "9988998899", "Male"),
        (9, "Harshil", "Khakhi", "Rajkot", "harshil@atmiyauni.edu", "9988998899", "Male"),
        (10, "Kairavi", "Parsana", "Rajkot", "kairavi@atmiyauni.edu", "9988998899", "Female"),
        (11, "Hemang", "Baldha", "Rajkot", "hemang@atmiyauni.edu", "9988998899", "Male")
    ]

    cursor.executemany(query, data)
    connection.commit()

    print("New records created successfully")

    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
