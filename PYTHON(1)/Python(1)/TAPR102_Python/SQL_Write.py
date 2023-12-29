import time
from itertools import count
import numpy as np
import pyodbc
import datetime
import string
import secrets
import pandas as pd

conn = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn)

def alphanumeric_random(num):
    num = 10
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    return str(res)

for i in range(1):
    if connection:
        print("We are connected")
    else:
        print("Failed to connect")

    cursor = connection.cursor()

    for i in count():
        A1 = i
        A2 = np.random.choice(list(string.ascii_letters))
        A3 = np.random.choice(list(string.ascii_letters))
        A4 = alphanumeric_random(10)
        A5 = np.random.randint(1,20)
        A6 = np.random.randint(200, 250)
        A7 = np.random.randint(1, 10)
        A8 = np.random.randint(10, 20)
        A9 = np.random.randint(20, 30)
        A10 = np.random.randint(10, 20)
        A11 = np.random.randint(20, 30)
        A12 = np.random.randint(1, 10)
        A13 = np.random.randint(30, 40)
        A14 = np.random.randint(20, 30)
        A15 = np.random.randint(40, 50)

        table_name = 'TAPR102.dbo.TAPR102'

        columns = ['Sl_No', '[User]', 'OperationalShift', 'StackBarcodeData', 'Robot_Cycle_Time', 'GlueWeight',
                   'Spare01', 'Spare02', 'Spare03', 'Spare04', 'Spare05',
                   'Spare06', 'Spare07', 'Spare08', 'Spare09']

        # Adjust the number of placeholders and values
        values = (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15)
        #placeholders = ', '.join(['?' for _ in range(len(columns))])

        SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(SQLCommand, values)

        connection.commit()
        time.sleep(0.1)

connection.close()
