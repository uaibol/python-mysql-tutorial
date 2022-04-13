import mysql.connector

def insert(name, birthday, score):
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pass",
            database="db_name")

    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO person (name, birthday, score) VALUES (%s, %s, %s)", (name, birthday, score))

    if cursor.lastrowid:
        print("last insert id", cursor.lastrowid)
    else:
        print("last insert id not found")
    conn.commit()

    conn. close()

if __name__ == "__main__":
    insert("Monty Python", "1969-10-05", 100)
