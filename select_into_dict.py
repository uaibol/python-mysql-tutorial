import mysql.connector as mysql

connection_params = {
        "host":"localhost",
        "user":"root",
        "password":"pass123",
        "database":"db_name",
        "raise_on_warnings":True
}

conn = mysql.connect(**connection_params)

cursor = conn.cursor(dictionary=True)
rows = cursor.execute("SELECT * FROM person")

for row in rows:
    print(row)

cursor.close()
conn.close()

