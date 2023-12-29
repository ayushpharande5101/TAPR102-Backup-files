import time
import pyodbc
from pymodbus.client import ModbusTcpClient
import struct
import pandas as pd

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

def concatenate(list1):
    a = bin(list1[0])[2:]
    b = bin(list1[1])[2:]

    concatenated_binary = '0' + b + '0' + a
    return concatenated_binary

def binary_to_float_ieee754(binary_string):
    # Convert the binary string to a 32-bit unsigned integer
    ieee754_bits = int(binary_string, 2)

    # Pack the integer into binary data
    packed_data = struct.pack('!I', ieee754_bits)

    # Unpack the binary data as a float number
    float_number = struct.unpack('!f', packed_data)[0]

    return float_number

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
IP_Address = '192.168.10.10'  # 192.168.10.10
client = ModbusTcpClient(IP_Address)
print(client.connect())
time.sleep(1)

while True:
    Z = client.read_holding_registers(0, 1)
    print("Value Before Condition: ",Z.registers[0])
    if Z.registers[0] == 1:
        a = []
        b = []
        c = []
        d = []

        print("Value After: ",Z.registers[0])

        for j in range(5):   #LENGTH = 5
            x1 = client.read_holding_registers(1+j, 5)
            A1 = x1.registers[0]
            a.append(A1)
        for k in range(1):   #LENGTH = 1
            x2 = client.read_holding_registers(6+k, 1)
            A2 = x2.registers[0]
            b.append(A2)
        for s in range(25):  #LENGTH = 25
            x3 = client.read_holding_registers(7+s,25)
            A3 = x3.registers[0]
            c.append(A3)

        for t in range(1):  #LENGTH = 1
            x4 = client.read_holding_registers(33+t,2)
            D = x4.registers[0]
        for n in range(2):
            x5 = client.read_holding_registers(34+n,2)
            E = x5.registers[0]
            d.append(E)
        for v in range(1):
            x6 = client.read_holding_registers(36+v,2)
            F = x6.registers[0]
            x7 = client.read_holding_registers(37+v,2)
            G = x7.registers[0]
        print(d)
        E1 = concatenate(d)
        E2 = binary_to_float_ieee754(E1)
        A = for_list(a)
        B = for_list(b)
        C = for_list(c)
        table_name = 'TAPR102.dbo.Data_Log_Python'
        columns = ['[USER]','OperationalShift','StackBarcodeData','Robot_Cycle_Time','GlueWeight','Spare01','Spare02']
        values = (A,B,C,D,E2,F,G)
        SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(SQLCommand, values)

        if SQLCommand == f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?,?,?,?,?,?,?)":
            print(SQLCommand)
            client.write_registers(0, 0)

        connection.commit()

    time.sleep(2)

