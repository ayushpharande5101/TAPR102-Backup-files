import pandas as pd
import pyodbc

conn_str = 'DSN=Control;UID=username;PWD=password'

connection = pyodbc.connect(conn_str)

if connection:
    print("Connected to the database")
else:
    print("Failed to connect to the database")
    exit()

sql_query = '''
                select * from TAPR102.dbo.Table_2
            '''

df = pd.read_sql_query(sql_query, connection)

df.to_csv('D:\\PYTHON(1)\\Python_Project\\Ayush_Python3.csv', index=True)
