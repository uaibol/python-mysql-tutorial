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
cursor.execute("SELECT * FROM person WHERE score > %s", (min_score,))

size = 2

while True:
    rows = cursor.fetchmany(size)
    if not rows:
        break
    print(len(rows))
    for row in rows:
        print(row)
cursor.close()
conn.close()

