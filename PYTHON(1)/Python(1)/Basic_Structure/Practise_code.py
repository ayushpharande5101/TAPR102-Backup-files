import time

# from opcua import server

from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

IP_Address = '127.0.0.1'
client = ModbusTcpClient(IP_Address)

print("[+]Info : Connection : " + str(client.connect()))
