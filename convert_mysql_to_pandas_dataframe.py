import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd


connection_params = {
        "host":"localhost",
        "user":"root",
        "password":"aibar434",
        "database":"qazeng",
        "raise_on_warnings":True
}

connection = mysql.connect(**connection_params)
cursor = connection.cursor()
cursor.execute("SELECT * FROM phrases")

df = pd.DataFrame(cursor.fetchall())

connection.close()

#Display the data
df
df.drop_duplicates(subset=[1])
