from mysql.connector import connect, Error

try:
    with connect(host="localhost", user="root", password="pass123", database="db_name") as connection:
        print(connection)
except Error as e:
    print(e)

