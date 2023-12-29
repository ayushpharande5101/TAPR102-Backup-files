import time
import pyodbc
from pymodbus.client import ModbusTcpClient

def split_ascii_value(value):
    high_byte = value >> 8
    low_byte = value & 0xFF
    return high_byte, low_byte

def for_list(a):
    result = ""
    for i in a:
        value = i
        high_byte, low_byte = split_ascii_value(value)

        if (65 <= low_byte <= 90 or 48 <= low_byte <= 57) and low_byte != 0:
            result += chr(low_byte)
            #return chr(low_byte)

        if (65 <= high_byte <= 90 or 48 <= high_byte <= 57) and high_byte != 0:
            result += chr(high_byte)
            #return chr(high_byte)
    return result

# DATABASE CONNECTION
conn_str = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn_str)

if connection:
    print("Connected Successfully")
else:
    print("Failed to connect")

cursor = connection.cursor()
time.sleep(1)

# MODBUS SERVER CONNECTION
IP_Address = '127.0.0.1'  # 192.168.10.10
client = ModbusTcpClient(IP_Address)
print(client.connect())
time.sleep(1)

Z = client.read_holding_registers(0, 1)
print("Value Before Condition: ",Z.registers[0])
if Z.registers[0] == 1:
    a = []
    print("Condition Satisfied")
    for j in range(6):
        x1 = client.read_holding_registers(1+j, 4)
        A1 = x1.registers[0]
        a.append(A1)

    A = for_list(a)

    table_name = 'TAPR102.dbo.Data_Log_Python2'
    columns = ['StackBarcodeData']
    values = (A,)
    SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?)"
    cursor.execute(SQLCommand, values)

    if SQLCommand == f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?)":
        client.write_registers(0, 0)

    connection.commit()