import numpy as np
import pyodbc
import datetime
import string
import secrets
import pandas as pd
from pymodbus.client import ModbusTcpClient

#MODBUS CONNECTION
IP_Address = '192.168.10.10'  #192.168.10.10 , #127.0.0.1
client = ModbusTcpClient(IP_Address)
if client.connect():
    print(client.connect())
else:
    print("Not Connected")

#DATABASE CONNECTION
conn = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn)

def alphanumeric_random(num):
    num = 10
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    return str(res)

#ASCII VALUE
def split_ascii_value(value):

    high_byte = value >> 8
    low_byte = value & 0xFF
    return high_byte, low_byte

for r in x4:
    value = r
    high_byte, low_byte = split_ascii_value(value)
    #print(high_byte)  # 123
    #print(low_byte)  # 45

    if ((65 <= low_byte <= 90) or (48 <= low_byte <= 57)) and low_byte != 0:
        print(chr(low_byte), end="")

    if ((65 <= high_byte <= 90) or (48 <= high_byte <= 57)) and high_byte != 0:
        print(chr(high_byte))

#OverallCode
for j in range(1):
    if connection:
        print("We are connected")
    else:
        print("Failed to connect")
    cursor = connection.cursor()

for i in range(25):
    counts = 1
    A1 = client.read_holding_registers(1,counts)
    A2 = client.read_holding_registers(26,counts)
    A4 = client.read_holding_registers(76,counts)
    A5 = client.read_holding_registers(101,counts)
    A6 = client.read_holding_registers(126,counts)
    A7 = client.read_holding_registers(151,counts)
    A8 = client.read_holding_registers(176,counts)
    A9 = client.read_holding_registers(201,counts)
    A10 = client.read_holding_registers(226,counts)
    A11 = client.read_holding_registers(251,counts)
    A12 = client.read_holding_registers(276,counts)
    A13 = client.read_holding_registers(301,counts)
    A14 = client.read_holding_registers(326,counts)
    A15 = client.read_holding_registers(351,counts)
    for k in range(10):
        A3 = client.read_holding_registers(51 + k, counts)
    table_name = 'TAPR102.dbo.TAPR102'

    columns = ['Sl_No', '[User]', 'OperationalShift', 'StackBarcodeData', 'Robot_Cycle_Time', 'GlueWeight',
               'Spare01', 'Spare02', 'Spare03', 'Spare04', 'Spare05',
               'Spare06', 'Spare07', 'Spare08', 'Spare09']

    values = (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15)
    placeholders = ', '.join(['?' for _ in range(len(columns))])

    SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(SQLCommand, values)

    connection.commit()

#EXCELSHEET GENERATION
A = input("Enter P to Generate Excel Sheet: ")
if A == 'P':
    sql_query = '''
                    select * from TAPR102.dbo.TAPR102
                '''
    print(sql_query)
    df = pd.read_sql_query(sql_query, connection)

    df.to_csv('D:\\PYTHON(1)\\Python_Project\\TAPR102 Report.csv',index=True)
else:
    print("Canceled Generation ")





