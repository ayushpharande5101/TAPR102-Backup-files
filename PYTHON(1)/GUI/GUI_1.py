import struct

list1 = [18350, 17136]
# list1 = [-2621, 16880]

# Swapping values using if-else condition
if list1[0] < list1[1]:
    list1[0], list1[1] = list1[1], list1[0]
    if list1[0] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[2:]
    elif list1[1] < 0:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[3:]
    elif (list1[0] and list[1]) < 0:
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
    elif list1[0]< 0 and list[1] < 0:
        a = bin(list1[0])[3:]
        b = bin(list1[1])[3:]
    else:
        a = bin(list1[0])[2:]
        b = bin(list1[1])[2:]
    pass
print(a)
print(b)
concatenated_binary = '0' + b + '0' + a
print(concatenated_binary)

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



