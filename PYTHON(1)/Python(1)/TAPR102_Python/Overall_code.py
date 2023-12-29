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
def split_ascii_value(x4):

  high_byte = value >> 8
  low_byte = value & 0xFF
  return high_byte, low_byte

for i in x4:
    value = i
    high_byte, low_byte = split_ascii_value(value)
    #print(high_byte)  # 123
    #print(low_byte)  # 45

    if ((65 <= low_byte <= 90) or (48 <= low_byte <= 57)) and low_byte != 0:
        print(chr(low_byte), end="")

    if ((65 <= high_byte <= 90) or (48 <= high_byte <= 57)) and high_byte != 0:
        print(chr(high_byte))


#OverallCode
x1 = client.read_holding_registers(1,25)
x2 = client.read_holding_registers(26,25)
x3 = client.read_holding_registers(51,25)
x4 = client.read_holding_registers(76,25)
x5 = client.read_holding_registers(101,25)
x6 = client.read_holding_registers(126,25)
x7 = client.read_holding_registers(151,25)
x8 = client.read_holding_registers(176,25)
x9 = client.read_holding_registers(201,25)
x10 = client.read_holding_registers(226,25)
x11 = client.read_holding_registers(251,25)
x12 = client.read_holding_registers(276,25)
x13 = client.read_holding_registers(301,25)
x14 = client.read_holding_registers(326,25)
x15 = client.read_holding_registers(351,25)


for j in range(1):
    if connection:
        print("We are connected")
    else:
        print("Failed to connect")

    cursor = connection.cursor()

for i in range(25):
    A1 = x1[i]
    A2 = x2[i]
    A3 = x3[i]
    A4 = x4[i]
    A5 = x5[i]
    A6 = x6[i]
    A7 = x7[i]
    A8 = x8[i]
    A9 = x9[i]
    A10 = x10[i]
    A11 = x11[i]
    A12 = x12[i]
    A13 = x13[i]
    A14 = x14[i]
    A15 = x15[i]

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


