# Python MySQL Tutorial with Pandas Library

**1. Installation**

```python
>>> virtualenv venv
>>> source venv/bin/activate
>>> pip install pandas
>>> pip install mysql-connector-python

```

# 2. Establishing a Connection

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
# **3. CRUD Operations in MySQL**
	
	- Create Operation
	- Read Operation
	- Update Operation
	- Delete Operation

**3.1. Create Operation**
	
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

**3.2. Read Operation**

Syntax:

```mysql
USE db_name;
SELECT * FROM table_name;
```

**3.3. Update Operation**

There is  two statements are mostly used for Update Operation.
1. Alter Table Statement - This is the DDL statement (Data Definition Language) used to change the structure of the table.
2. Update Table Statement - This is the DML statement (Data Manipulating Language) used to alter the records.


Syntax: Alter table

```mysql
ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name;

ALTER TABLE table_name
MODIFY COLUMN column_name datatype;

```

Syntax: Update - The Update statement is used to modify the existing records in a table.

```mysql

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

```
Example:

```mysql
UPDATE table_name
SET column1 = "Person Name", column2 = "Person address",
WHERE id = 1;

```

**4. Delete Operation**

The `DELETE` statement is used to delete existing records in a table.

Syntax:

```mysql
DELETE FROM table_name WHERE condition;
```

Example:
```mysql
 DELETE FROM table_name WHERE column1='Person Name'; 
```

# 4. MySQL Joins
The joins are one of the advanced topics for MySQL berginners to grasp. On the other hand studying concepts of mathematical sets, unions, intersections, and their resulting Venn diagrams helpful to understanding mysql joins.
