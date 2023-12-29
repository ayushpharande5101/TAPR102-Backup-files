import struct

def concatenate(list1):
    if list1[0] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[2:]
    elif list1[1] < 0:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[3:]
    else:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[2:]

    concatenated_binary = '0' + b + '0' + a
    return concatenated_binary

A1 = [234, 32555]

B1 = concatenate(A1)
#---------------------------------------------------------------------------------------------------------------------
def binary_to_float_ieee754(binary_string):
    # Convert the binary string to a 32-bit unsigned integer
    ieee754_bits = int(binary_string, 2)

    # Pack the integer into binary data
    packed_data = struct.pack('!I', ieee754_bits)

    # Unpack the binary data as a float number
    float_number = struct.unpack('!f', packed_data)[0]

    return float_number
# Example usage:
binary_representation = B1  # Example binary string for 3.14
float_number = binary_to_float_ieee754(binary_representation)
print(float_number)

