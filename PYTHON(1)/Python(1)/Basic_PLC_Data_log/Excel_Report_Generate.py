import pandas as pd
import pyodbc

conn_str = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn_str)

if connection:
    print("We are connected")
else:
    print("Failed to connect")

sql_query = '''
               select * from TAPR102.dbo.Data_Log_Python
            '''
df = pd.read_sql_query(sql_query, connection)

df.to_csv('D:\\PYTHON(1)\\Python_Project\\TAPR102 Report1.csv', index=True)






