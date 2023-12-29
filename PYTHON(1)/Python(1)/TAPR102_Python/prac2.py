from pymodbus.client import ModbusTcpClient

IP_Address = '192.168.10.10'  #192.168.10.10
client = ModbusTcpClient(IP_Address)
print(client.connect())

def for_list(L):
    for i in L:
        print(i)

A1 = client.read_holding_registers(1,25)
A2 = client.read_holding_registers(26,25)
A3 = client.read_holding_registers(51,25)
A4 = client.read_holding_registers(76,25)
A5 = client.read_holding_registers(101,25)
A6 = client.read_holding_registers(126,25)
A7 = client.read_holding_registers(151,25)
A8 = client.read_holding_registers(176,25)
A9 = client.read_holding_registers(201,25)
A10 = client.read_holding_registers(226,25)
A11 = client.read_holding_registers(251,25)
A12 = client.read_holding_registers(276,25)
A13 = client.read_holding_registers(301,25)
A14 = client.read_holding_registers(326,25)
A15 = client.read_holding_registers(351,25)

for_list(A1)
for_list(A2)
for_list(A3)
for_list(A4)
for_list(A5)
for_list(A6)
for_list(A7)
for_list(A8)
for_list(A9)
for_list(A10)
for_list(A11)
for_list(A12)
for_list(A13)
for_list(A14)
for_list(A15)

k = result.registers

print(k)
value = k

def split_ascii_value(value):

  high_byte = value >> 8
  low_byte = value & 0xFF
  return high_byte, low_byte

for i in k:
    value = i
    high_byte, low_byte = split_ascii_value(value)
    #print(high_byte)  # 123
    #print(low_byte)  # 45

    if ((65 <= low_byte <= 90) or (48 <= low_byte <= 57)) and low_byte != 0:
        print(chr(low_byte), end="")

    if ((65 <= high_byte <= 90) or (48 <= high_byte <= 57)) and high_byte != 0:
        print(chr(high_byte), end="")


