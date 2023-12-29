import struct

def float_to_ieee754(value):
    # Pack the float into its IEEE 754 representation
    ieee754_representation = struct.pack('>f', value)
    # Convert the packed binary data to an integer for easy display
    ieee754_integer = int.from_bytes(ieee754_representation, byteorder='big', signed=False)
    return ieee754_representation, ieee754_integer

def ieee754_to_float(binary_code):
    # Convert the binary code to an integer
    ieee754_integer = int(binary_code, 2)
    # Pack the integer into its IEEE 754 representation
    ieee754_representation = ieee754_integer.to_bytes(4, byteorder='big')
    # Unpack the IEEE 754 representation to get the float value
    value = struct.unpack('>f', ieee754_representation)[0]
    return value

# Example usage
plc_float_value = 123.123
ieee754_representation, ieee754_integer = float_to_ieee754(plc_float_value)

print(f'Float Value: {plc_float_value}')
print(f'IEEE 754 Representation (Binary): {bin(ieee754_integer)}')
print(f'IEEE 754 Representation (Hex): {hex(ieee754_integer)}')

# Remove the '0b' prefix and get the last 32 bits
binary_code = bin(ieee754_integer)[2:].zfill(32)
# binary_code = '01100110001011001101110010111010'

print(f'32-bit Binary Code: {binary_code}')

# Convert the 32-bit binary code back to a float
converted_value = ieee754_to_float(binary_code)
print(f'Converted Value: {converted_value}')