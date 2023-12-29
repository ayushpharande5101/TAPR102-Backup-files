import pyodbc
from datetime import datetime

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server= AYUSHP-DELL\\SQLEXPRESS03;'
                      'Database = TAPR102_1;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Define the SQL command to create a table
table_exists_query = ("IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Data_Log1') "
                      "CREATE TABLE Data_Log1 (DateTime DATETIME PRIMARY KEY, [User] NVARCHAR(50), [Operational Shift] NVARCHAR(50),"
                      " [Station Name] NVARCHAR(50), [Process Name] NVARCHAR(50), [Battery ID] NVARCHAR(50), "
                      "[Cycle Time] INT, [Glue Weight] FLOAT  );")

start = start_date_entry.get_date().strftime('%Y-%m-%d')  # Getting an entry for date to be fetched
end = end_date_entry.get_date().strftime('%Y-%m-%d')
sql = "SELECT * FROM master.dbo.Data_Log_1 WHERE DateTime BETWEEN ? AND ?"
cursor = conn.execute(sql, (start, end))

cursor.execute(table_exists_query)

# Commit the changes and close the connection
conn.commit()
conn.close()