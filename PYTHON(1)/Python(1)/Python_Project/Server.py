#pip install pyModbusTCP

from pyModbusTCP.client import ModbusClient

# Modbus TCP server details
SERVER_HOST = '192.168.1.100'  # Replace with your server's IP address
SERVER_PORT = 502  # Default Modbus TCP port is 502

# Create a Modbus TCP client
client = ModbusClient()

# Specify the Modbus TCP server details
client.host(SERVER_HOST)
client.port(SERVER_PORT)

# Open the connection to the Modbus TCP server
if not client.is_open():
    if not client.open():
        print("Unable to connect to Modbus TCP server")
        exit(1)

# Read holding registers (for example, holding register 0, quantity 5)
start_register = 0
quantity = 5
regs = client.read_holding_registers(start_register, quantity)

# Check if the read was successful
if regs:
    print(f"Read successful! Holding registers: {regs}")
else:
    print("Failed to read holding registers")

# Close the Modbus TCP connection
client.close()