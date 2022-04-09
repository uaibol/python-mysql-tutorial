from mysql.connector import connect, Error

try:
    connection_params = {
            "host":"localhost",
            "user":"root",
            "password":"pass123",
            "database":"db_name"
    }
    with connect(**connection_params) as connection:
        if connection.is_connected():
            print(connection.get_server_info())
            cursor = connection.cursor()
            cursor.execute("select database();")
            db = cursor.fetchone()
            print("You are connected to the database: ", db)
except Error as e:
    print(e)

