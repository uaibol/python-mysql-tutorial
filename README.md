# Python MySQL Tutorial with Pandas Library

**1. Installation**

```python
>>> virtualenv venv
>>> source venv/bin/activate
>>> pip install pandas
>>> pip install mysql-connector-python

```

**2. Establishing a Connection**

```python
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


```
**3. CRUD Operations in MySQL**
	
	- Create Operation
	- Read Operation
	- Update Operation
	- Delete Operation

3.1. Create Operation
	
Syntax:

```mysql
CREATE TABLE table_name (column_name column_type constraints);

```
Parameters:<br>
	1. **column_name** - Name of the particular column<br>
	2. **column_type** - DataType of the column. DataType can be: **char(), varchar(), int(), float(),** etc.<br>
	3. **constraints** - In order to give restrictions to particular column constraints are used. Constraints can be - **not null, primary key, foreign key,** etc.<br>

**Example:**<br>
```mysql

USE db_name;
CREATE TABLE table_name(
	id int NOT NULL AUTO_INCREMENT,
	name varchar(50) NOT NULL,
	age int NOT NULL,
	PRIMARY KEY (id)
);

```

3.2. Read Operation

Syntax:

```mysql
USE db_name;
SELECT * FROM table_name;
```

3.3. Update Operation

There is  two commands are mostly used for Update Operation.
1. Alter Table Command - This is the DDL command (Data Definition Language) used to change the structure of the table.
2. Update Table Command - This is the DML command (Data Manipulating Language) used to alter the records.


Syntax:

```mysql
ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name;

ALTER TABLE table_name
MODIFY COLUMN column_name datatype

```
