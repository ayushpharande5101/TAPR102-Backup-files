from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder


IP_Address = "192.168.10.10"  # 192.168.10.10
client = ModbusTcpClient(IP_Address)
connected = client.connect()
print(f"Connected: {connected}")

if connected:
    result = client.read_holding_registers(1, 20)
    registers = result.registers

    for register in registers:
        # Split bytes
        high_byte = register >> 8
        low_byte = register & 0xFF

        # Check if printable characters
        is_printable_low = (low_byte >= 32 and low_byte <= 126) or low_byte == 9
        is_printable_high = (high_byte >= 32 and high_byte <= 126) or high_byte == 9

        # Print characters if both bytes are printable
        if is_printable_low and is_printable_high:
            print(chr(low_byte), end="")
            print(chr(high_byte), end="")

    client.close()

