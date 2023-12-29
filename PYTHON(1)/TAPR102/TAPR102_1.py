import time
import pyodbc
from pymodbus.client import ModbusTcpClient
import struct
import pandas as pd
import datetime

#--------------------------------------------------------------------------------------------------------------------------------
def split_ascii_value(value):
    high_byte = value >> 8
    low_byte = value & 0xFF
    return high_byte, low_byte
#-------------------------------------------------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------------
def concatenate(list1):
    a = bin(list1[0])[2:]
    b = bin(list1[1])[2:]

    concatenated_binary = '0' + b + '0' + a
    return concatenated_binary
#---------------------------------------------------------------------------------------------------------------------
def binary_to_float_ieee754(binary_string):
    # Convert the binary string to a 32-bit unsigned integer
    ieee754_bits = int(binary_string, 2)

    # Pack the integer into binary data
    packed_data = struct.pack('!I', ieee754_bits)

    # Unpack the binary data as a float number
    float_number = struct.unpack('!f', packed_data)[0]

    return float_number
#-------------------------------------------------------------------------------------------------------------------------

# DATABASE CONNECTION
conn_str = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn_str)

if connection:
    print("Connected Successfully")
else:
    print("Failed to connect")

cursor = connection.cursor()

time.sleep(1)

#---------------------------------------------------------------------------------------------------------------------
# MODBUS SERVER CONNECTION
IP_Address = '192.168.10.10'  # 192.168.10.10
client = ModbusTcpClient(IP_Address)
print(client.connect())
time.sleep(1)

#----------------------------------------------------------------------------------------------------------------------
k = 1
while k<=1000:
    Z = client.read_holding_registers(0, 1)
    print("Value Before Condition: ",Z.registers[0])
    if Z.registers[0] == 1:
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []

        b1 = []

        print("Value After: ",Z.registers[0])

        #Values Stored in Registers
        y1 = 1   #1-5 USER
        y2 = 6   #6-10 Operational Shift
        y3 = 11  #11-30 Station Name
        y4 = 31  #31-50 Process Name
        y5 = 51  #51-70 Battery ID
        y6 = 71  #71-72 Glue Weight
        y7 = 73  #73 Cycle Weight

        for j1 in range(5):   #LENGTH = 5
            x1 = client.read_holding_registers(y1+j1, 5)
            A1 = x1.registers[0]
            a1.append(A1)

        for j2 in range(5):   #LENGTH = 5
            x2 = client.read_holding_registers(y2+j2, 1)
            A2 = x2.registers[0]
            a2.append(A2)

        for j3 in range(20):  #LENGTH = 20
            x3 = client.read_holding_registers(y3+j3,25)
            A3 = x3.registers[0]
            a3.append(A3)

        for j4 in range(20): #LENGTH = 20
            x4 = client.read_holding_registers(y4+j4,25)
            A4 = x4.registers[0]
            a4.append(A4)

        for j5 in range(20): #LENGTH = 20
            x5 = client.read_holding_registers(y5+j5,25)
            A5 = x5.registers[0]
            a5.append(A5)

        for n in range(2):  #LENGTH = 2
            x6 = client.read_holding_registers(y6+n,2)
            E = x6.registers[0]
            b1.append(E)

        for v in range(1):  #LENGTH = 1
            x7 = client.read_holding_registers(y7+v,2)
            CYCLE_WEIGHT = x7.registers[0]


        DATETIME = datetime.datetime.now()  #DateTime
        USER = for_list(a1)
        OPERATIONAL_SHIFT = for_list(a2)
        STATION_NAME = for_list(a3)
        PROCESS_NAME = for_list(a4)
        BATTERY_ID = for_list(a5)

        E1 = concatenate(b1)
        GLUE_WEIGHT = binary_to_float_ieee754(E1)

        table_name = 'TAPR102_1.dbo.Table_1'

        columns = ['DateTime','[User]', '[Operational Shift]', '[Station Name]', '[Process Name]', '[Battery ID]', '[Glue Weight]',
                   '[Cycle Weight]']

        values = (DATETIME, USER, OPERATIONAL_SHIFT, STATION_NAME, PROCESS_NAME, BATTERY_ID, GLUE_WEIGHT, CYCLE_WEIGHT)

        SQLCommand = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(SQLCommand, values)

        print("Data Entered Successfully")
        # if f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES (?,?,?,?,?,?,?,?)":
        #     print("Data Entered Successfully")
        #     client.write_registers(0, 0)

        connection.commit()

    k = k + 1