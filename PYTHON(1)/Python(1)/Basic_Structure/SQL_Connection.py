import pyodbc

# #SQL_CONNECTION
# conn_str = 'DSN=Control;UID='';PWD='''
# connection = pyodbc.connect(conn_str)
#
# if connection:
#     print("We are connected")
# else:
#     print("Failed to connect")
#
# sql = '''\
# SELECT TOP (1000) [Part_Id]
#       ,[Name]
#       ,[Outputs]
# FROM [TAPR102].[dbo].[Table_2]
# '''
#
# curser = connection.execute(sql)
#
# for i in curser:
#     print(i[0], end="  "),print(i[1],end=" "),print(i[2])


conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server= AYUSHP-DELL\\SQLEXPRESS03;'
                      'Database = TAPR102_1;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()





