from pymodbus.client import ModbusTcpClient
import struct

IP_Address = '192.168.10.10'  # 192.168.10.10
client = ModbusTcpClient(IP_Address)
print(client.connect())
x = []
for i in range(2):

    x1 = client.read_holding_registers(72+i, 2)
    A1 = x1.registers[0]
    x.append(A1)
print(x)

list1 = x
if list1[0] < list1[1]:
    list1[0], list1[1] = list1[1], list1[0]
    if list1[0] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[2:]
    elif list1[1] < 0:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[3:]
    elif (list1[0] < 0) and (list[1] < 0):
        a = bin(list1[0])[3:]
        b = bin(list1[1])[3:]
    else:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[2:]

else:
    if list1[0] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[2:]
    elif list1[1] < 0:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[3:]
    elif (list1[0] < 0) and (list[1] < 0):
        a = bin(list1[0])[3:]
        b = bin(list1[1])[3:]
    else:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[2:]
    pass
print(a)
print(b)
concatenated_binary = '0' + b + '0' + a


def binary_to_float_ieee754(binary_string):
    # Convert the binary string to a 32-bit unsigned integer
    ieee754_bits = int(binary_string, 2)

    # Pack the integer into binary data
    packed_data = struct.pack('!I', ieee754_bits)

    # Unpack the binary data as a float number
    float_number = struct.unpack('!f', packed_data)[0]

    return float_number

# Example usage:
binary_representation = concatenated_binary   # Example binary string for 3.14
float_number = binary_to_float_ieee754(binary_representation)
print(float_number)
