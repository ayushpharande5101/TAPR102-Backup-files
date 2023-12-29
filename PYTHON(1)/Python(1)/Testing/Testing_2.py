import numpy as np
import pyodbc

conn_str = 'DSN=Control;UID='';PWD='''  # Please replace with your actual connection string
connection = pyodbc.connect(conn_str)

if connection:
    print("Connected to the database")
else:
    print("Failed to connect")

cursor = connection.cursor()

table_name = 'TAPR102.dbo.Table_01'

columns = ['Part_Id', 'Alpha', '[User]']

x1 = [10, 20, 30]
x2 = [34, 89, 23]
x3 = [67, 98, 56]

x = tuple(x1)
y = tuple(x2)
z = tuple(x3)
values = (x1,x2,x3)

insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?)"

# Use executemany to insert multiple rows
cursor.execute(insert_query, values)

connection.commit()

# Close the cursor and connection when done
cursor.close()
connection.close()
