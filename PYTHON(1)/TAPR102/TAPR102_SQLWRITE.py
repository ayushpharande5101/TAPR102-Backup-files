import time

import numpy as np
import pyodbc

conn = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn)

for i in range(10):
    if connection:
        print("We are connected")
    else:
        print("Failed to connect")

    cursor = connection.cursor()

    USER = np.random.rand()
    OPERATIONAL_SHIFT = np.random.rand()
    STATION_NAME = np.random.rand()
    PROCESS_NAME = np.random.rand()
    BATTERY_ID = np.random.rand()
    GLUE_WEIGHT = np.random.rand()
    CYCLE_TIME = np.random.rand()

    table_name = 'TAPR102_1.dbo.Table_2'

    columns = ['[User]', '[Operational Shift]', '[Station Name]', '[Process Name]','[Battery ID]','[Cycle Time]','[Glue Weight]']

    values = (USER, OPERATIONAL_SHIFT, STATION_NAME, PROCESS_NAME, BATTERY_ID, CYCLE_TIME, GLUE_WEIGHT )

    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?)"

    cursor.execute(insert_query, values)

    time.sleep(2)
    connection.commit()


