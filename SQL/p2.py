import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="google",
    database="mydb"  # optional: specify database name if connecting to a specific database
)

print(myconn)  # Print the connection object
