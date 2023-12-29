import datetime
import time
import numpy as np
import pyodbc

def sqlwrite():
    conn = 'DSN=Control;UID='';PWD='''
    connection = pyodbc.connect(conn)

    for i in range(1000):
        # if connection:
        #     print("We are connected")
        # else:
        #     print("Failed to connect")

        cursor = connection.cursor()

        DATETIME = datetime.datetime.now()
        USER = np.random.rand()
        OPERATIONAL_SHIFT = np.random.rand()
        STATION_NAME = np.random.rand()
        PROCESS_NAME = np.random.rand()
        BATTERY_ID = np.random.rand()
        GLUE_WEIGHT = np.random.rand()
        CYCLE_TIME = np.random.rand()

        table_name = 'TAPR102_1.dbo.Table_1'

        columns = ['DateTime', '[User]', '[Operational Shift]', '[Station Name]', '[Process Name]', '[Battery ID]',

                   '[Cycle Time]','[Glue Weight]']

        values = (DATETIME, USER, OPERATIONAL_SHIFT, STATION_NAME, PROCESS_NAME, BATTERY_ID, CYCLE_TIME, GLUE_WEIGHT )

        SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(SQLCommand, values)

        if SQLCommand == f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)":
            print("Data Inserted")


        # if f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?,?,?,?,?,?,?,?)":
        #     print("Data Entered Successfully")
        #     client.write_registers(0, 0)

        time.sleep(2)

        connection.commit()

sqlwrite()