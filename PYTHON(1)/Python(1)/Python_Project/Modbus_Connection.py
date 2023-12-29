import time
import binascii
# from opcua import server

from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

IP_Address = '192.168.10.10'  #192.168.10.10
client = ModbusTcpClient(IP_Address)
print(client.connect())

# result = client.read_holding_registers(1,1)
# k = result.registers
# print(k)
#
# print(k)
#
# value = k
#
# def split_ascii_value(value):
#
#   high_byte = value >> 8
#   low_byte = value & 0xFF
#   return high_byte, low_byte
#
# # Example usage:
# low = []
# high = []
# for i in k:
#   high_byte, low_byte = split_ascii_value(value)
#   high.append(high_byte)
#   low.append(low_byte)
#
# print(low)
# print(high)
#
# print(chr(low_byte), end="")
# print(chr(high_byte))
# print(i)
#
# high_byte, low_byte = split_ascii_value(value)
# print(high_byte)  # 123
# print(low_byte)  # 45
#
# print(chr(low_byte),end="")
# print(chr(high_byte))

"""
client.write_registers(0,25)
client.write_registers(1,34)
client.write_registers(2,90)
client.write_registers(3,45)
client.write_registers(4,78)
client.write_registers(5,61)
client.write_registers(6,99)

result = client.read_holding_registers(0,7)
print(result.registers)


#print("[+]Info : Connection : " + str(client.connect()))

read_value = client.read_holding_registers(0,2)
dint_decoder = BinaryPayloadDecoder.fromRegisters(read_value.registers,Endian.Big, wordorder=Endian.Little)
value = dint_decoder.decode_32bit_int()
print(value)
"""
