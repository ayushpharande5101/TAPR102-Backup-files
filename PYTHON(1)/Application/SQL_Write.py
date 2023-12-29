import datetime
import time
import numpy as np
import pyodbc

# Establish a connection
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=AYUSHP-DELL\\SQLEXPRESS03;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

table_exists_query = ("IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Data_Log1') "
                      "CREATE TABLE Data_Log1 (DateTime DATETIME, [User] NVARCHAR(50), [Operational Shift] NVARCHAR(50),"
                      " [Station Name] NVARCHAR(50), [Process Name] NVARCHAR(50), [Battery ID] NVARCHAR(50), "
                      "[Cycle Time] INT, [Glue Weight] FLOAT );")

cursor.execute(table_exists_query)
def sqlwrite():
    try:
        for i in range(1000):
            # Use a context manager for the cursor
            with conn.cursor() as cursor:
                DATETIME = datetime.datetime.now()
                USER = np.random.rand()
                OPERATIONAL_SHIFT = np.random.rand()
                STATION_NAME = np.random.rand()
                PROCESS_NAME = np.random.rand()
                BATTERY_ID = np.random.rand()
                GLUE_WEIGHT = np.random.rand()
                CYCLE_TIME = np.random.randint(1000)

                table_name = 'master.dbo.Data_Log1'

                columns = ['DateTime', '[User]', '[Operational Shift]', '[Station Name]', '[Process Name]', '[Battery ID]',
                           '[Cycle Time]', '[Glue Weight]']

                values = (DATETIME, USER, OPERATIONAL_SHIFT, STATION_NAME, PROCESS_NAME, BATTERY_ID, CYCLE_TIME, GLUE_WEIGHT)

                SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

                # Execute the command
                cursor.execute(SQLCommand, values)

                # Check the row count to verify if the data was inserted
                if cursor.rowcount > 0:
                    print("Data Inserted")


            # Commit the transaction
            conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection outside the loop
        conn.close()

# Call the function
sqlwrite()