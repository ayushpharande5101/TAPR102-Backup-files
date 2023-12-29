import pyodbc

table_name = 'TAPR102_1.dbo.Table_1'
columns = ['DateTime', '[User]', '[Operational Shift]', '[Station Name]', '[Process Name]', '[Battery ID]',
           '[Cycle Time]', '[Glue Weight]']
values = (DATETIME, USER, OPERATIONAL_SHIFT, STATION_NAME, PROCESS_NAME, BATTERY_ID, CYCLE_TIME, GLUE_WEIGHT)

# Connect to the database
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Check if the table exists
cursor.execute(f"IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}') CREATE TABLE {table_name} ({', '.join(columns)});")

# Commit the transaction
conn.commit()

# Now, you can perform the insertion
SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cursor.execute(SQLCommand, values

cursor.execute(f"IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}') CREATE TABLE {table_name} ({', '.join(columns)});")