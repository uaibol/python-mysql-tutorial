import mysql.connector as mysql

connection_params = {
        "host":"localhost",
        "user":"root",
        "password":"pass123",
        "database":"db_name",
        "raise_on_warnings":True
}

conn = mysql.connect(**connection_params)

cursor = conn.cursor()
cursor.execute("SELECT * FROM table_name")

row = cursor.fetchone()
print(row)
#cursor.close() #mysql.connector.errors.InternalError: Unread result found.

#Select more data

while True:
    row = cursor.fetchone()
    if not row:
        break
    print(row)

cursor.close()
conn.close()


conn.close()
