import mysql.connector
try:
    con=mysql.connector.connect(host="localhost", user="root",passwd="charan")
    print("successfully connection established!")
except mysql.connector.DatabaseError as d:
    print("Problem in mysql:",d)